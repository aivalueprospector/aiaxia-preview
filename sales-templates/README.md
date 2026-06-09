# Sales templates

Sales materials for **ProAsiste** and **EduAsiste**. **The content HTML pages are the
source of truth.** They live in `sales/<brand>/` and are served as web pages. Office
downloads (`.docx`) are generated **on demand** from those pages.

## Source of truth

```
sales/<brand>/*.html          content pages (web-first, print-ready)  ← edit these
   │
   ├─ <head> declares the hub card:
   │     <meta name="card-title" content="Twin Feature Guide">
   │     <meta name="card-desc"  content="...">
   │     <meta name="card-order" content="10">
   │
   ├─ gen_hubs.py       scans the pages → writes sales/index.html + brand hubs
   └─ make_download.py  pandoc HTML→docx (on demand) → sales/templates/
```

Add a content page with `card-*` meta → it appears on the brand hub automatically. There is
no second list of materials to keep in sync.

## Common tasks

```bash
# Regenerate the hub index pages (run after adding/editing a content page)
python3 gen_hubs.py

# Build a download for one or more pages, on demand (page-stem = filename without .html)
python3 make_download.py proasiste one-pager
python3 make_download.py eduasiste competitive security-faq
```

`gen_hubs.py` gives every card a **View** link, and a **Download** link only if a matching
`sales/templates/<brand>-<stem>.docx` exists. `make_download.py` builds that file and re-runs
`gen_hubs.py`, so the Download button appears once the download exists.

## Layout

| Path | What |
|---|---|
| `sales/<brand>/*.html` | **source of truth** — content pages + their card meta |
| `sales/<brand>/index.html` | generated hub (do not hand-edit; rerun `gen_hubs.py`) |
| `sales/templates/` | on-demand `.docx` downloads (only what `make_download.py` has built) |
| `gen_hubs.py` | discover cards from HTML → write hub pages |
| `make_download.py` | HTML → branded `.docx` on demand |
| `branding.py`, `brands.json` | build the brand reference docs used for HTML→docx styling |
| `reference-docs/` | brand-styled pandoc reference docs (`<brand>.docx`) |
| `sheets/*.py` | openpyxl ROI calculator + pipeline tracker (`.xlsx`, separate) |

## Conventions

- **Edit content in the HTML pages.** Hub `index.html` files are generated output.
- A content page joins its brand hub by declaring `card-title` / `card-desc` / `card-order`
  meta. No meta → not listed.
- Placeholders for reps stay as literal `{{Field}}` text in the HTML; they carry through to
  the generated `.docx`.
- Decks (`.pptx`) and sheets (`.xlsx`) are not produced by `make_download.py` (pandoc
  HTML→pptx is lossy). Build those separately; `gen_hubs.py` still links any that exist in
  `sales/templates/`.

## History

The previous markdown → Office pipeline (`build.py`, `templates.map`, `src/en/*.md`,
`tokens.json`, `en/`) was retired in favor of this HTML-first flow. It is documented in
issue #19 and recoverable from git history if needed.
