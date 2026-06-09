#!/usr/bin/env python3
"""
Generate an Office download for a sales material ON DEMAND, from its content HTML.

HTML is the source of truth. This converts a content page to a branded .docx via pandoc,
drops it in sales/templates/, and re-runs gen_hubs so the card gains a Download button.

Usage:
    python make_download.py <brand> <page-stem> [<page-stem> ...]
    python make_download.py proasiste one-pager
    python make_download.py eduasiste competitive security-faq

  brand:     proasiste | eduasiste
  page-stem: the content file name without .html (e.g. "one-pager" for one-pager.html)

Output: sales/templates/<brand>-<page-stem>.docx  (named so gen_hubs auto-detects it)

Notes:
- Needs pandoc on PATH. Styling comes from reference-docs/<brand>.docx (run branding.py once
  if reference-docs/ is empty).
- Slides (the deck) are not produced here — pandoc HTML->pptx is lossy. Build decks separately.
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SALES = HERE.parent / "sales"
TEMPLATES = SALES / "templates"
REFDIR = HERE / "reference-docs"


def make(brand, stem):
    src = SALES / brand / f"{stem}.html"
    if not src.exists():
        print(f"  ERROR: {src.relative_to(SALES.parent)} not found", file=sys.stderr)
        return None
    ref = REFDIR / f"{brand}.docx"
    if not ref.exists():
        print(f"  ERROR: {ref} missing — run branding.py first", file=sys.stderr)
        return None
    TEMPLATES.mkdir(exist_ok=True)
    out = TEMPLATES / f"{brand}-{stem}.docx"
    cmd = ["pandoc", str(src), "-f", "html", "-t", "docx",
           "--reference-doc", str(ref), "-o", str(out)]
    subprocess.run(cmd, check=True)
    print(f"  built {out.relative_to(SALES.parent)}")
    return out


def main():
    args = sys.argv[1:]
    if len(args) < 2 or args[0] not in ("proasiste", "eduasiste"):
        print(__doc__)
        sys.exit(1)
    brand, stems = args[0], args[1:]
    built = [m for s in stems if (m := make(brand, s))]
    if built:
        import gen_hubs
        gen_hubs.main()
    print(f"Done: {len(built)} download(s) for {brand}")


if __name__ == "__main__":
    main()
