# Sales templates (issue #31)

Branded, copy-and-customize sales templates for **AI Value Prospectors / ProAsiste / EduAsiste**,
delivered as Office files that import into Google Workspace (`.docx`→Docs, `.xlsx`→Sheets,
`.pptx`→Slides). A rep opens one, **File → Make a copy**, replaces the highlighted `{{fields}}`,
and **Download → PDF**.

Outputs live in [`en/`](en). `gen_hubs.py` publishes them into `sales/templates/` and lists every
material on its brand page (`sales/index.html`, `sales/proasiste/`, `sales/eduasiste/`).

## Build

```bash
# from repo root; needs pandoc + python-docx + openpyxl + python-pptx
python3 -m venv --system-site-packages ../.venv-templates
../.venv-templates/bin/pip install python-pptx
../.venv-templates/bin/python branding.py            # reference-docs/{brand}.docx|.pptx
../.venv-templates/bin/python build.py               # Docs + Slides from templates.map
../.venv-templates/bin/python sheets/roi_calculator.py
../.venv-templates/bin/python sheets/pipeline_tracker.py
../.venv-templates/bin/python gen_hubs.py            # publishes sales/templates/ + brand hub pages
```

## Layout

| Path | What |
|---|---|
| `brands.json` | per-brand colors, logo, domain |
| `branding.py` | builds branded pandoc reference docs (colors, fonts, logo header, `Placeholder` highlight style) |
| `tokens.json` | per-artifact `{{field}}` lists (drives the auto "HOW TO USE" box) |
| `templates.map` | driver rows: `slug\|fmt\|brand\|src_md\|title` |
| `build.py` | normalizes tokens → highlighted spans, prepends HOW-TO box, runs pandoc |
| `sheets/*.py` | openpyxl ROI calculator + pipeline tracker (live formulas, dropdowns) |
| `src/en/` | source markdown (English) |
| `en/` | generated `.docx` / `.xlsx` / `.pptx` |
| `gen_hubs.py` | publishes `en/` → `sales/templates/` and regenerates the brand hub pages (common + ProAsiste + EduAsiste), each listing all that brand's materials with View / Download actions |

## Conventions

- Placeholders: `{{Field Name}}` → rendered as a highlighted run reps replace. Never wrapped inside code spans.
- Each Doc/Slides opens with an auto-generated **HOW TO USE** callout listing that file's fields.
- Sheets expose inputs as yellow cells with dropdown validation; rate card / waiver logic from
  `twincloud/docs/PRICING-SPEC.md`.

## Deferred (out of scope for #31)

- **Drive delivery** — uploading to a shared Drive folder, "Anyone with link – Viewer", and the
  one-click `…/copy` share links. The index page is built to hold those links when a folder exists.
- **Spanish (`es/`)** — pipeline is language-agnostic; translate `src/en/*.md` → `src/es/*.md` and
  rebuild. Hold until the English set is approved.
