#!/usr/bin/env python3
"""
Generate the brand-oriented sales hub pages AND publish the downloadable files.

  sales/index.html            — common / cross-twin materials + entry links to each brand
  sales/proasiste/index.html  — ALL ProAsiste materials (view + download in one list)
  sales/eduasiste/index.html  — ALL EduAsiste materials

Each material is one card showing the actions available for it: "View" (browser HTML)
and/or "Download" (Office file that imports into Google Docs/Sheets/Slides). There is
no separate templates page — every brand's full kit lives on its brand page.

Also copies the built Office files from en/ into sales/templates/ for direct download.
Run after build.py + sheets/*.py.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SALES = HERE.parent / "sales"
EXT_LABEL = {"docx": "Doc", "xlsx": "Sheet", "pptx": "Slides"}

# A material: (swatch, title, desc, view_href_or_None, download_filename_or_None)
COMMON = [
    ("↔", "Knowledge Demo Guide", "Tab-by-tab platform demo script (Import · View · Task · Verify) — works for both brands.",
     "knowledge-demo-guide.html", "knowledge-demo-guide.docx"),
]

BRANDS = {
    "proasiste": {
        "display": "ProAsiste", "tag": "Business", "domain": "proasiste.com",
        "cls": "pro", "swatch": "Pro",
        "blurb": "Everything for the business product — owner-operators and the small teams around them.",
        "materials": [
            ("One-Pager", "Business leave-behind: owner twin + team twins, five day-one things, opener + close. Print-ready.",
             "one-pager.html", "proasiste-one-pager.docx"),
            ("Sales Email Templates", "Business outreach by angle — time-saver, competitor, knowledge-loss. Copy, customize, send.",
             "email-templates.html", "proasiste-email-templates.docx"),
            ("Two-Twins Pitch Blurbs", "Short ready-to-send emails leading with the two-twins idea (owner twin + team twins). Pick a version, fill the fields, send.",
             "pitch-blurbs.html", "proasiste-pitch-blurbs.docx"),
            ("Quick Reference Card", "One-page cheat sheet: pitch, tabs, pain→response, tiers. Print-friendly.",
             "quick-reference.html", "proasiste-quick-reference.docx"),
            ("Competitive Positioning", "Battle cards vs. ChatGPT / Copilot — their argument, your response, differentiator tables.",
             "competitive.html", "proasiste-competitive.docx"),
            ("Security FAQ", "Tier × infrastructure security, what's included, KloudStax compliance path.",
             "security-faq.html", "proasiste-security-faq.docx"),
            ("Customer Personas", "Business buyer profiles with pains, demo focus, and closing language.",
             None, "proasiste-personas.docx"),
            ("How Two Twins Work Together — Deck", "~8-slide business deck with speaker notes. Read the outline in the browser or download the editable deck.",
             "deck.html", "proasiste-pitch-deck.pptx"),
        ],
    },
    "eduasiste": {
        "display": "EduAsiste", "tag": "Education", "domain": "eduasiste.org",
        "cls": "edu", "swatch": "Edu",
        "blurb": "Everything for the education product — families, tutors, homeschoolers and small schools.",
        "materials": [
            ("One-Pager", "Education leave-behind: parent twin + child's learning twin, five day-one things, opener + close. Print-ready.",
             "one-pager.html", "eduasiste-one-pager.docx"),
            ("Sales Email Templates", "Parent / tutor / school outreach. Copy, customize, send.",
             "email-templates.html", "eduasiste-email-templates.docx"),
            ("Two-Twins Pitch Blurbs", "Short ready-to-send emails leading with the two-twins idea (parent twin + child's twin). Pick a version, fill the fields, send.",
             "pitch-blurbs.html", "eduasiste-pitch-blurbs.docx"),
            ("Quick Reference Card", "One-page cheat sheet for parent/school calls. Print-friendly.",
             "quick-reference.html", "eduasiste-quick-reference.docx"),
            ("Competitive Positioning", "Battle cards vs. generic AI, grade portals, content libraries, tutoring.",
             "competitive.html", "eduasiste-competitive.docx"),
            ("Security FAQ", "FERPA / COPPA / GDPR, minors' data, the transparency pillar.",
             "security-faq.html", "eduasiste-security-faq.docx"),
            ("Customer Personas", "Five education buyer profiles with demo focus + closing language.",
             None, "eduasiste-personas.docx"),
            ("How Two Twins Work Together — Deck", "~8-slide education deck with speaker notes. Read the outline in the browser or download the editable deck.",
             "deck.html", "eduasiste-pitch-deck.pptx"),
        ],
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
    footer{text-align:center;color:var(--muted);font-size:13px;padding:28px 24px;border-top:1px solid var(--border);}
    footer a{color:var(--ACCENT);text-decoration:none;}
"""


def material_card(swatch, title, desc, view, download, view_prefix, dl_prefix):
    acts = []
    if view:
        acts.append(f'<a class="view" href="{view_prefix}{view}">View →</a>')
    if download:
        ext = download.rsplit(".", 1)[1]
        acts.append(f'<a class="dl" href="{dl_prefix}{download}" download>Download {EXT_LABEL[ext]}</a>')
    actions = "\n                ".join(acts)
    return f'''            <div class="card">
                <div class="swatch">{swatch}</div>
                <h2>{title}</h2>
                <div class="desc">{desc}</div>
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

HOWTO = ('<div class="howto"><b>Downloads:</b> drag a downloaded file into Google Drive '
         '(it converts to a native Doc / Sheet / Slides), then <b>File → Make a copy</b>, '
         'replace every <b>highlighted {{field}}</b>, and <b>Download → PDF</b> to send.</div>')


def build_common():
    header = '''    <header>
        <span class="wordmark"><span class="mark">Ai</span><span class="name">AI Value Prospectors</span></span>
        <h1>Sales materials</h1>
        <p>Pick your brand for its full kit, or grab a shared cross-twin asset below.</p>
    </header>'''
    entries = []
    for key, b in BRANDS.items():
        entries.append(f'''            <a class="brand-entry {b['cls']}" href="{key}/">
                <div class="be-top"><div class="be-chip">{b['swatch']}</div>
                    <div><h2>{b['display']}</h2><div class="be-sub">{b['tag']} · {b['domain']}</div></div></div>
                <div class="be-desc">{b['blurb']}</div>
                <div class="be-go">Open {b['display']} materials →</div>
            </a>''')
    cards = "\n".join(material_card(*m, view_prefix="", dl_prefix="templates/") for m in COMMON)
    main = f'''        <p class="section-label"><span class="pip"></span>Choose your brand</p>
        <div class="brand-grid">
{chr(10).join(entries)}
        </div>

        <p class="section-label"><span class="pip"></span>Cross-twin &amp; platform <span class="hint">— shared by both brands</span></p>
        {HOWTO}
        <div class="card-grid">
{cards}
        </div>'''
    foot = 'AI Value Prospectors · internal sales enablement · Source: <a href="https://github.com/aivalueprospector/product-research">product-research</a>'
    (SALES / "index.html").write_text(shell("aivp", "AI Value Prospectors — Sales materials", header, main, foot))


def build_brand(key, b):
    header = f'''    <header>
        <span class="wordmark"><span class="mark">{b['swatch']}</span><span class="name">{b['display']}</span></span>
        <h1>{b['display']} — Sales materials</h1>
        <p>{b['blurb']}</p>
        <a class="back" href="../index.html">&larr; All sales materials</a>
    </header>'''
    cards = "\n".join(material_card(b["swatch"], *m, view_prefix="", dl_prefix="../templates/")
                      for m in b["materials"])
    main = f'''        <p class="section-label"><span class="pip"></span>{b['display']} materials</p>
        {HOWTO}
        <div class="card-grid">
{cards}
        </div>'''
    foot = f'{b["display"]} · {b["domain"]} · internal sales enablement · <a href="../index.html">All materials</a>'
    out = SALES / key / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(shell(b["cls"], f"{b['display']} — Sales materials", header, main, foot))


def publish_files():
    pub = SALES / "templates"
    pub.mkdir(exist_ok=True)
    n = 0
    for f in sorted((HERE / "en").glob("*")):
        if f.suffix in (".docx", ".xlsx", ".pptx"):
            shutil.copy2(f, pub / f.name)
            n += 1
    return n


def main():
    n = publish_files()
    build_common()
    for key, b in BRANDS.items():
        build_brand(key, b)
    print(f"published {n} files to sales/templates/; wrote index.html + 2 brand hubs")


if __name__ == "__main__":
    main()
