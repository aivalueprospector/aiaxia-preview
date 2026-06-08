#!/usr/bin/env python3
"""
Build branded sales templates (.docx / .pptx) from source markdown.

Driven by templates.map (pipe-delimited): slug|fmt|brand|src_md|title
  fmt:  D = .docx (Google Docs)   P = .pptx (Google Slides)
  brand: aivp | proasiste | eduasiste
  src_md: path relative to sales-templates/ (usually src/en/<file>.md)

Pipeline per row:
  1. normalize legacy placeholders -> {{Field}}
  2. wrap every {{Field}} in a pandoc span with custom-style "Placeholder"
  3. prepend an auto-generated "HOW TO USE" callout listing the file's fields
  4. pandoc --reference-doc=reference-docs/<brand>.{docx|pptx}

Usage:  python build.py [--lang en] [slug ...]
Sheets are built separately by sheets/*.py.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
REFDIR = HERE / "reference-docs"
ASSETS = REPO  # logos resolved relative to repo root

TOKENS = json.loads((HERE / "tokens.json").read_text())
BRANDS = json.loads((HERE / "brands.json").read_text())

# legacy bracket/brace tokens -> canonical
ALIASES = {
    "name": "Prospect Name",
    "first name": "Prospect Name",
    "company name": "Company",
    "link": "Demo Link",
    "your name": "Rep Name",
}

HOWTO_EN = (
    "**HOW TO USE THIS TEMPLATE.** 1. *File → Make a copy.* "
    "2. Rename it for your prospect. 3. Replace every highlighted "
    "**{{field}}**. 4. Delete this box. 5. *File → Download → PDF* to send."
)


def normalize_tokens(md):
    # {{name}} / {{link}} style aliases
    def brace_sub(m):
        inner = m.group(1).strip()
        return "{{" + ALIASES.get(inner.lower(), inner) + "}}"
    md = re.sub(r"\{\{\s*([^}]+?)\s*\}\}", brace_sub, md)

    # single-bracket [Field] placeholders (Title-Case, NOT a markdown link [x](...))
    def bracket_sub(m):
        inner = m.group(1).strip()
        return "{{" + ALIASES.get(inner.lower(), inner) + "}}"
    md = re.sub(r"\[([A-Z][A-Za-z0-9 ./&'’-]*?)\](?!\()", bracket_sub, md)
    return md


def wrap_placeholders(md):
    # {{Field}} -> [{{Field}}]{custom-style="Placeholder"}  (keeps braces visible + highlighted)
    # but NEVER inside code (fenced ``` or inline `…`), where span syntax would render literally.
    sub = lambda s: re.sub(
        r"\{\{\s*([^}]+?)\s*\}\}",
        lambda m: '[{{' + m.group(1).strip() + '}}]{custom-style="Placeholder"}',
        s,
    )
    segments = re.split(r"(```.*?```|`[^`]*`)", md, flags=re.S)
    return "".join(seg if i % 2 else sub(seg) for i, seg in enumerate(segments))


def artifact_type(slug):
    return re.sub(r"^(aivp|proasiste|eduasiste)-", "", slug)


def howto_block(slug):
    fields = TOKENS.get(artifact_type(slug), [])
    lines = ["> " + HOWTO_EN]
    if fields:
        toks = " · ".join("{{" + f + "}}" for f in fields)
        lines.append(">")
        lines.append("> **Fields in this template:** " + toks)
    else:
        lines.append(">")
        lines.append("> *This is a reference cheat sheet. No fields to replace, so customize freely.*")
    return "\n".join(lines) + "\n\n"


def strip_provenance(md):
    # drop leading "> _..._" provenance/migration notes
    out = []
    for ln in md.splitlines():
        if ln.strip().startswith("> _") and ("igrated" in ln or "ebranded" in ln or
                                             "ariant" in ln or "endered" in ln or "pdated" in ln):
            continue
        out.append(ln)
    return "\n".join(out)


def strip_first_h1(md):
    out, done = [], False
    for ln in md.splitlines():
        if not done and re.match(r"^#\s+\S", ln):
            done = True
            continue
        out.append(ln)
    return "\n".join(out)


def build_one(slug, fmt, brand, src, title):
    src_path = (HERE / src).resolve()
    md = src_path.read_text()
    md = strip_provenance(md)
    md = strip_first_h1(md)  # metadata title renders it; avoid duplicate
    md = normalize_tokens(md)
    md = howto_block(slug) + md
    md = wrap_placeholders(md)

    ext = "docx" if fmt == "D" else "pptx"
    ref = REFDIR / f"{brand}.{ext}"
    out = HERE / "en" / f"{slug}.{ext}"
    out.parent.mkdir(exist_ok=True)

    cmd = [
        "pandoc", "-", "-f", "gfm+bracketed_spans+fenced_divs",
        "--reference-doc", str(ref),
        "--resource-path", str(ASSETS),
        "--metadata", f"title={title}",
        "-o", str(out),
    ]
    if fmt == "P":
        cmd += ["--slide-level", "2"]
    subprocess.run(cmd, input=md, text=True, check=True)

    # lint: any unconverted single-bracket tokens or stray braces survive?
    raw = out.read_bytes()
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not REFDIR.exists() or not any(REFDIR.iterdir()):
        import branding
        branding.main()

    rows = []
    for line in (HERE / "templates.map").read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        slug, fmt, brand, src, title = line.split("|", 4)
        if args and slug not in args:
            continue
        rows.append((slug, fmt, brand, src, title))

    built = []
    for slug, fmt, brand, src, title in rows:
        try:
            out = build_one(slug, fmt, brand, src, title)
            built.append(out.name)
            print(f"  built {out.name}")
        except subprocess.CalledProcessError as e:
            print(f"  FAILED {slug}: {e}", file=sys.stderr)
    print(f"Done: {len(built)} files in en/")


if __name__ == "__main__":
    main()
