#!/usr/bin/env python3
"""
Generate the brand sales hub pages from the content HTML — HTML is the source of truth.

  sales/index.html            — brand chooser (+ any cross-twin materials)
  sales/proasiste/index.html  — every ProAsiste material, discovered from sales/proasiste/*.html
  sales/eduasiste/index.html  — every EduAsiste material, discovered from sales/eduasiste/*.html

Each content page under sales/<brand>/ (except index.html) declares its card in <head>:

    <meta name="card-title" content="Twin Feature Guide">
    <meta name="card-desc"  content="What the business twin does ...">
    <meta name="card-order" content="10">

A page with a card-title becomes a card (sorted by card-order). Every card gets a
"View" link. It also gets a "Download" link IFF a matching Office file already exists in
sales/templates/ (named "<brand>-<page-stem>.<ext>"). Downloads are produced on demand by
make_download.py — this script never builds them, it just reflects what's present.

Add a content page with card meta -> it appears on the hub. No second list to maintain.
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SALES = HERE.parent / "sales"
TEMPLATES = SALES / "templates"
EXT_LABEL = {"docx": "Doc", "xlsx": "Sheet", "pptx": "Slides"}

# Brand-level presentation only (not a material list — materials are discovered from HTML).
BRANDS = {
    "proasiste": {
        "display": "ProAsiste", "tag": "Business", "domain": "proasiste.com",
        "cls": "pro", "swatch": "Pro", "anchor": "#proasiste",
        "blurb": "Everything for the business product. Owner-operators and the small teams around them.",
    },
    "eduasiste": {
        "display": "EduAsiste", "tag": "Education", "domain": "eduasiste.org",
        "cls": "edu", "swatch": "Edu", "anchor": "#edu-institution",
        "blurb": "Everything for the education product. Families, tutors, homeschoolers, and small schools.",
    },
}

CSS = """
    :root{--aivp:#E8B547;--aivp-dark:#92700f;--pro:#CFB382;--pro-dark:#92700f;--edu:#2EA3F2;--edu-dark:#1d6fb0;
    --bg:#0F1115;--card-bg:#181B22;--text:#F3F4F6;--text-soft:#C2C6CC;--muted:#9AA0A6;--border:#2A2E37;}
    *{box-sizing:border-box;}
    body{margin:0;font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;background:var(--bg);color:var(--text);min-height:100vh;display:flex;flex-direction:column;}
    header{padding:40px 24px 18px;text-align:center;border-bottom:1px solid var(--border);}
    .wordmark{display:inline-flex;align-items:center;gap:10px;margin-bottom:12px;}
    .wordmark .mark{min-width:38px;height:38px;padding:0 10px;border-radius:9px;background:var(--ACCENT);color:#0F1115;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:15px;}
    .wordmark .name{font-size:14px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--ACCENT);}
    header h1{margin:0;font-size:30px;font-weight:800;letter-spacing:-.02em;}
    header p{margin:10px auto 0;color:var(--muted);font-size:15px;max-width:600px;}
    header a.back{display:inline-block;margin-top:14px;color:var(--text-soft);text-decoration:none;font-size:13px;font-weight:600;}
    header a.back:hover{color:var(--ACCENT);}
    main{flex:1;max-width:1040px;margin:0 auto;padding:28px 24px;width:100%;}
    .section-label{font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--text-soft);margin:34px 0 0;display:flex;align-items:center;gap:10px;}
    .section-label:first-of-type{margin-top:6px;}
    .section-label .pip{width:10px;height:10px;border-radius:50%;background:var(--ACCENT);}
    .section-label .hint{font-weight:500;text-transform:none;letter-spacing:0;color:var(--muted);font-size:13px;}
    .card-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:18px;margin-top:16px;}
    .card{background:var(--card-bg);border:1px solid var(--border);border-radius:14px;padding:22px;display:flex;flex-direction:column;gap:8px;}
    .card .swatch{align-self:flex-start;min-width:38px;height:32px;padding:0 10px;border-radius:9px;background:var(--ACCENT);color:#0F1115;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:800;}
    .card h2{margin:0;font-size:17px;font-weight:700;}
    .card .desc{color:var(--text-soft);font-size:13.5px;line-height:1.55;}
    .actions{display:flex;gap:8px;margin-top:auto;padding-top:14px;flex-wrap:wrap;}
    .actions a{font-size:12.5px;font-weight:700;text-decoration:none;padding:6px 13px;border-radius:999px;border:1px solid var(--border);transition:border-color 120ms,background 120ms,color 120ms;}
    .actions a.view{color:var(--ACCENT);}
    .actions a.view:hover{border-color:var(--ACCENT);background:rgba(255,255,255,.03);}
    .actions a.dl{color:var(--text-soft);}
    .actions a.dl:hover{border-color:var(--text-soft);color:var(--text);}
    .brand-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px;margin-top:8px;}
    .brand-entry{display:flex;flex-direction:column;gap:6px;padding:26px;border-radius:16px;text-decoration:none;color:inherit;border:1px solid var(--border);background:var(--card-bg);transition:transform 120ms,border-color 120ms,box-shadow 120ms;}
    .brand-entry:hover{transform:translateY(-3px);box-shadow:0 14px 34px rgba(0,0,0,.4);}
    .brand-entry.pro:hover{border-color:var(--pro);}
    .brand-entry.edu:hover{border-color:var(--edu);}
    .brand-entry .be-top{display:flex;align-items:center;gap:12px;}
    .brand-entry .be-chip{min-width:46px;height:46px;padding:0 12px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:15px;color:#0F1115;}
    .brand-entry.pro .be-chip{background:var(--pro);}
    .brand-entry.edu .be-chip{background:var(--edu);color:#06243b;}
    .brand-entry h2{margin:0;font-size:21px;font-weight:800;}
    .brand-entry .be-sub{font-size:13px;color:var(--muted);}
    .brand-entry .be-desc{font-size:14px;color:var(--text-soft);line-height:1.55;margin-top:4px;}
    .brand-entry .be-go{margin-top:8px;font-size:13px;font-weight:700;}
    .brand-entry.pro .be-go{color:var(--pro);}
    .brand-entry.edu .be-go{color:var(--edu);}
    .howto{background:var(--card-bg);border:1px solid var(--border);border-left:3px solid var(--ACCENT);border-radius:12px;padding:16px 20px;margin:18px 0 0;font-size:13.5px;color:var(--text-soft);line-height:1.6;}
    .howto b{color:var(--text);}
    .demos-cta{display:flex;align-items:center;gap:16px;margin-top:16px;padding:18px 22px;border-radius:14px;text-decoration:none;color:inherit;border:1px solid var(--border);background:linear-gradient(135deg,rgba(232,181,71,.10),rgba(46,163,242,.10));transition:transform 120ms,border-color 120ms,box-shadow 120ms;}
    .demos-cta:hover{transform:translateY(-2px);border-color:var(--ACCENT);box-shadow:0 10px 28px rgba(0,0,0,.32);}
    .demos-cta .dc-icon{flex:none;width:44px;height:44px;border-radius:12px;background:var(--ACCENT);color:#0F1115;display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:800;}
    .demos-cta .dc-text{display:flex;flex-direction:column;gap:2px;}
    .demos-cta .dc-text strong{font-size:16px;}
    .demos-cta .dc-text span{font-size:13px;color:var(--text-soft);}
    .demos-cta .dc-go{margin-left:auto;font-size:13px;font-weight:700;color:var(--ACCENT);}
    footer{text-align:center;color:var(--muted);font-size:13px;padding:28px 24px;border-top:1px solid var(--border);}
    footer a{color:var(--ACCENT);text-decoration:none;}
"""

HOWTO = ('<div class="howto"><b>Downloads:</b> drag a downloaded file into Google Drive '
         '(it converts to a native Doc / Sheet / Slides), then <b>File → Make a copy</b>, '
         'replace every <b>highlighted {{field}}</b>, and <b>Download → PDF</b> to send.</div>')

_META = lambda name, txt: (re.search(rf'<meta\s+name="{name}"\s+content="([^"]*)"', txt) or [None, None])[1]


def scan_cards(brand):
    """Discover material cards from sales/<brand>/*.html via their card-* meta tags."""
    cards = []
    for page in sorted((SALES / brand).glob("*.html")):
        if page.name == "index.html":
            continue
        head = page.read_text()[:4000]
        title = _META("card-title", head)
        if not title:
            print(f"  skip {brand}/{page.name}: no card-title meta")
            continue
        desc = _META("card-desc", head) or ""
        order = _META("card-order", head)
        order = int(order) if order and order.isdigit() else 9999
        # explicit card-download meta wins (handles stem != filename, e.g. deck -> pitch-deck);
        # otherwise auto-detect <brand>-<stem>.<ext> in sales/templates/
        explicit = _META("card-download", head)
        if explicit and (TEMPLATES / explicit).exists():
            download = explicit
        else:
            download = find_download(brand, page.stem)
        cards.append({"title": title, "desc": desc, "order": order,
                      "view": page.name, "download": download})
    cards.sort(key=lambda c: (c["order"], c["title"]))
    return cards


def find_download(brand, stem):
    """Return the templates/ filename for this page if a built Office file exists, else None."""
    for ext in ("docx", "pptx", "xlsx"):
        f = TEMPLATES / f"{brand}-{stem}.{ext}"
        if f.exists():
            return f.name
    return None


def material_card(swatch, card, view_prefix="", dl_prefix="../templates/"):
    acts = [f'<a class="view" href="{view_prefix}{card["view"]}">View →</a>']
    if card["download"]:
        ext = card["download"].rsplit(".", 1)[1]
        acts.append(f'<a class="dl" href="{dl_prefix}{card["download"]}" download>Download {EXT_LABEL[ext]}</a>')
    actions = "\n                ".join(acts)
    return f'''            <div class="card">
                <div class="swatch">{swatch}</div>
                <h2>{card["title"]}</h2>
                <div class="desc">{card["desc"]}</div>
                <div class="actions">
                {actions}
                </div>
            </div>'''


def shell(accent_var, title, header_html, main_html, foot):
    css = CSS.replace("var(--ACCENT)", f"var(--{accent_var})")
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
    <meta name="robots" content="noindex, nofollow">
    <title>{title}</title>
    <style>{css}    </style>
</head>
<body>
{header_html}
    <main>
{main_html}
    </main>
    <footer>{foot}</footer>
</body>
</html>
'''


def demos_cta(href, subtitle):
    return (f'<a class="demos-cta" href="{href}">'
            f'<div class="dc-icon">&#9654;</div>'
            f'<div class="dc-text"><strong>Twin Demos</strong><span>{subtitle}</span></div>'
            f'<div class="dc-go">Open &rarr;</div></a>')


def build_brand(key, b):
    header = f'''    <header>
        <span class="wordmark"><span class="mark">{b['swatch']}</span><span class="name">{b['display']}</span></span>
        <h1>{b['display']}: Sales materials</h1>
        <p>{b['blurb']}</p>
        <a class="back" href="../index.html">&larr; All sales materials</a>
    </header>'''
    cards = scan_cards(key)
    cards_html = "\n".join(material_card(b["swatch"], c) for c in cards)
    howto = HOWTO if any(c["download"] for c in cards) else ""
    demos = demos_cta(f"../../demos/index.html{b['anchor']}",
                      f"Jump to the live {b['display']} demo twins. Demo data only.")
    main = f'''        <p class="section-label"><span class="pip"></span>Live demos</p>
        {demos}

        <p class="section-label"><span class="pip"></span>{b['display']} materials</p>
        {howto}
        <div class="card-grid">
{cards_html}
        </div>'''
    foot = f'{b["display"]} · {b["domain"]} · internal sales enablement · <a href="../index.html">All materials</a>'
    out = SALES / key / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(shell(b["cls"], f"{b['display']}: Sales materials", header, main, foot))
    n_dl = sum(1 for c in cards if c["download"])
    print(f"  {key}: {len(cards)} cards ({n_dl} with downloads)")


def build_common():
    header = '''    <header>
        <span class="wordmark"><span class="mark">Ai</span><span class="name">AI Value Prospectors</span></span>
        <h1>Sales materials</h1>
        <p>Pick your brand for its full kit.</p>
    </header>'''
    entries = []
    for key, b in BRANDS.items():
        entries.append(f'''            <a class="brand-entry {b['cls']}" href="{key}/">
                <div class="be-top"><div class="be-chip">{b['swatch']}</div>
                    <div><h2>{b['display']}</h2><div class="be-sub">{b['tag']} · {b['domain']}</div></div></div>
                <div class="be-desc">{b['blurb']}</div>
                <div class="be-go">Open {b['display']} materials →</div>
            </a>''')
    demos = demos_cta("../demos/index.html",
                      "Explore the live, interactive demo twins for both brands. Demo data only.")
    main = f'''        <p class="section-label"><span class="pip"></span>Choose your brand</p>
        <div class="brand-grid">
{chr(10).join(entries)}
        </div>

        <p class="section-label"><span class="pip"></span>Live demos</p>
        {demos}'''
    foot = 'AI Value Prospectors · internal sales enablement · Source: <a href="https://github.com/aivalueprospector/aiaxia-preview">aiaxia-preview</a>'
    (SALES / "index.html").write_text(shell("aivp", "AI Value Prospectors: Sales materials", header, main, foot))


def main():
    build_common()
    for key, b in BRANDS.items():
        build_brand(key, b)
    print("wrote index.html + 2 brand hubs (cards discovered from sales/<brand>/*.html)")


if __name__ == "__main__":
    main()
