#!/usr/bin/env python3
"""
Generate the brand-oriented sales hub pages:
  sales/index.html            — common / cross-twin assets + entry links to each brand
  sales/proasiste/index.html  — ProAsiste reference pages + downloadable templates
  sales/eduasiste/index.html  — EduAsiste reference pages + downloadable templates

Single source of truth for all three. Run after gen_index.py (which publishes the
Office files into sales/templates/).
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
SALES = HERE.parent / "sales"
FMT = {"docx": ("Doc", "Google Docs"), "xlsx": ("Sheet", "Google Sheets"),
       "pptx": ("Slides", "Google Slides")}

# ---------- content model ----------
# HTML reference page: (href, swatch, title, desc)
# Download: (filename-in-templates/, title, desc)

COMMON_PAGES = [
    ("cross-twin-one-pager.html", "↔", "Cross-Twin One-Pager",
     "Both-brands leave-behind: EduAsiste and ProAsiste day-one pillars side by side, with an opener and close for reps. Print-ready (Letter)."),
    ("knowledge-demo-guide.html", "↔", "Knowledge Sales Demo Guide",
     "Tab-by-tab walkthrough of the Knowledge platform (Import · View · Task · Verify) — the same UI behind both brands."),
    ("cross-twin-slides.html", "↔", "How Two Twins Work Together — Slides",
     "8-slide deck outline (~7 min) with speaker notes. Built to get to the demo, then to the ask."),
    ("cross-twin-email-blurbs.html", "↔", "Email-Ready Blurbs — Cross-Twin",
     "Three ready-to-send blurbs at three lengths: cold outreach, warm intro, school/tutor prospect."),
]
COMMON_DOWNLOADS = [
    ("aivp-one-pager.docx", "One-Pager (both brands)", "EduAsiste + ProAsiste pillars with a rep contact line."),
    ("aivp-email-templates.docx", "Cross-Twin Email Templates", "Five outreach emails (education + business) plus tips."),
    ("knowledge-demo-guide.docx", "Knowledge Demo Guide", "Platform demo script for either brand."),
    ("aivp-pitch-deck.pptx", "Two-Twins Pitch Deck", "~8-slide cross-brand deck with speaker notes."),
    ("aivp-pricing-roi-calculator.xlsx", "Pricing & ROI Calculator", "Tier + seats → Year-1 and ongoing cost, certification-waiver math."),
    ("aivp-pipeline-tracker.xlsx", "Sales Pipeline Tracker", "Prospect → Pro → Member stages, auto est. value, summary."),
]

BRANDS = {
    "proasiste": {
        "display": "ProAsiste", "tag": "Business", "domain": "proasiste.com",
        "cls": "pro", "swatch": "Pro",
        "blurb": "Sales materials for the business product — owner-operators and the small teams around them.",
        "pages": [
            ("one-pager.html", "ProAsiste One-Pager", "Business leave-behind: owner twin + team twins, five day-one things, opener + close. Print-ready."),
            ("email-templates.html", "Sales Email Templates", "Business outreach by angle — time-saver, competitor, knowledge-loss. Copy, customize, send."),
            ("quick-reference.html", "Quick Reference Card", "One-page cheat sheet: pitch, tabs, pain→response, tiers. Print-friendly."),
            ("competitive.html", "Competitive Positioning", "Battle cards vs. ChatGPT / Copilot — their argument, your response, differentiator tables."),
            ("security-faq.html", "Security FAQ", "Tier × infrastructure security, what's included, KloudStax compliance path."),
        ],
        "downloads": [
            ("proasiste-one-pager.docx", "One-Pager", "Business leave-behind. Make a copy, fill fields, export PDF."),
            ("proasiste-email-templates.docx", "Email Templates", "Business outreach with highlighted fill-in fields."),
            ("proasiste-quick-reference.docx", "Quick Reference Card", "Print-friendly cheat sheet."),
            ("proasiste-competitive.docx", "Competitive Positioning", "Battle cards vs. ChatGPT / Copilot."),
            ("proasiste-security-faq.docx", "Security FAQ", "Tiered security + KloudStax compliance."),
            ("proasiste-personas.docx", "Customer Personas", "Business buyer profiles with demo focus + closing language."),
            ("proasiste-pitch-deck.pptx", "Pitch Deck", "~8-slide business deck with speaker notes."),
            ("proasiste-pricing-roi-calculator.xlsx", "Pricing & ROI Calculator", "Tier + seats → cost with certification-waiver math."),
        ],
    },
    "eduasiste": {
        "display": "EduAsiste", "tag": "Education", "domain": "eduasiste.org",
        "cls": "edu", "swatch": "Edu",
        "blurb": "Sales materials for the education product — families, tutors, homeschoolers and small schools.",
        "pages": [
            ("one-pager.html", "EduAsiste One-Pager", "Education leave-behind: parent twin + child's learning twin, five day-one things, opener + close. Print-ready."),
            ("email-templates.html", "Sales Email Templates", "Parent / tutor / school outreach. Copy, customize, send."),
            ("quick-reference.html", "Quick Reference Card", "One-page cheat sheet for parent/school calls. Print-friendly."),
            ("competitive.html", "Competitive Positioning", "Battle cards vs. generic AI, grade portals, content libraries, tutoring."),
            ("security-faq.html", "Security FAQ", "FERPA / COPPA / GDPR, minors' data, the transparency pillar."),
        ],
        "downloads": [
            ("eduasiste-one-pager.docx", "One-Pager", "Education leave-behind. Make a copy, fill fields, export PDF."),
            ("eduasiste-email-templates.docx", "Email Templates", "Parent / tutor / school outreach with fill-in fields."),
            ("eduasiste-quick-reference.docx", "Quick Reference Card", "Print-friendly cheat sheet."),
            ("eduasiste-competitive.docx", "Competitive Positioning", "Battle cards vs. ed-tech alternatives."),
            ("eduasiste-security-faq.docx", "Security FAQ", "FERPA / COPPA / GDPR + transparency."),
            ("eduasiste-personas.docx", "Customer Personas", "Five education buyer profiles with demo focus + closing language."),
            ("eduasiste-pitch-deck.pptx", "Pitch Deck", "~8-slide education deck with speaker notes."),
            ("eduasiste-pricing-roi-calculator.xlsx", "Pricing & ROI Calculator", "Tier + seats → cost with certification-waiver math."),
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
    .wordmark .mark{width:38px;height:38px;border-radius:9px;background:var(--ACCENT);color:#0F1115;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:16px;}
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
    .card-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px;margin-top:16px;}
    .card{background:var(--card-bg);border:1px solid var(--border);border-radius:14px;padding:22px;text-decoration:none;color:inherit;display:flex;flex-direction:column;gap:8px;transition:transform 120ms,box-shadow 120ms,border-color 120ms;}
    .card:hover{transform:translateY(-2px);box-shadow:0 10px 28px rgba(0,0,0,.35);border-color:var(--ACCENT);}
    .card .swatch{align-self:flex-start;min-width:40px;height:34px;padding:0 10px;border-radius:9px;background:var(--ACCENT);color:#0F1115;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:800;}
    .card h2{margin:0;font-size:17px;font-weight:700;}
    .card .desc{color:var(--text-soft);font-size:13.5px;line-height:1.55;}
    .card .meta{margin-top:auto;padding-top:12px;font-size:12px;color:var(--muted);}
    .card .meta code{font-family:ui-monospace,Menlo,monospace;color:var(--text-soft);}
    .brand-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px;margin-top:8px;}
    .brand-entry{display:flex;flex-direction:column;gap:6px;padding:26px;border-radius:16px;text-decoration:none;color:inherit;border:1px solid var(--border);background:var(--card-bg);transition:transform 120ms,border-color 120ms,box-shadow 120ms;}
    .brand-entry:hover{transform:translateY(-3px);box-shadow:0 14px 34px rgba(0,0,0,.4);}
    .brand-entry.pro:hover{border-color:var(--pro);}
    .brand-entry.edu:hover{border-color:var(--edu);}
    .brand-entry .be-top{display:flex;align-items:center;gap:12px;}
    .brand-entry .be-chip{width:46px;height:46px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:15px;color:#0F1115;}
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


def page_card(href, swatch, title, desc):
    return f'''            <a class="card" href="{href}">
                <div class="swatch">{swatch}</div>
                <h2>{title}</h2>
                <div class="desc">{desc}</div>
            </a>'''


def dl_card(prefix, fname, title, desc, swatch):
    ext = fname.rsplit(".", 1)[1]
    badge, native = FMT[ext]
    return f'''            <a class="card" href="{prefix}{fname}" download>
                <div class="swatch">{badge}</div>
                <h2>{title}</h2>
                <div class="desc">{desc}</div>
                <div class="meta">Downloads <code>{fname}</code> → opens in {native}</div>
            </a>'''


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


def build_common():
    header = '''    <header>
        <span class="wordmark"><span class="mark">Ai</span><span class="name">AI Value Prospectors</span></span>
        <h1>Sales materials</h1>
        <p>Shared, cross-twin assets plus everything for each brand. Internal working copies; not customer-facing unless noted.</p>
    </header>'''
    # brand entries
    entries = []
    for key, b in BRANDS.items():
        entries.append(f'''            <a class="brand-entry {b['cls']}" href="{key}/">
                <div class="be-top"><div class="be-chip">{b['swatch']}</div>
                    <div><h2>{b['display']}</h2><div class="be-sub">{b['tag']} · {b['domain']}</div></div></div>
                <div class="be-desc">{b['blurb']}</div>
                <div class="be-go">Open {b['display']} materials →</div>
            </a>''')
    pages = "\n".join(page_card(*p) for p in COMMON_PAGES)
    dls = "\n".join(dl_card("templates/", *d, "Doc") for d in COMMON_DOWNLOADS)
    main = f'''        <p class="section-label"><span class="pip"></span>Choose your brand</p>
        <div class="brand-grid">
{chr(10).join(entries)}
        </div>

        <p class="section-label"><span class="pip"></span>Cross-twin &amp; platform <span class="hint">— common to both brands</span></p>
        <div class="card-grid">
{pages}
        </div>

        <p class="section-label"><span class="pip"></span>Common downloadable templates <span class="hint">— make a copy, fill fields, export PDF</span></p>
        <div class="howto"><b>How to use:</b> download a file, drag it into Google Drive (it converts to a native Doc / Sheet / Slides), then <b>File → Make a copy</b>. Replace every <b>highlighted {{{{field}}}}</b> and <b>Download → PDF</b>. See the <a href="templates.html" style="color:var(--aivp)">full template library →</a> for every brand.</div>
        <div class="card-grid">
{dls}
        </div>'''
    foot = 'AI Value Prospectors · internal sales enablement · Source: <a href="https://github.com/aivalueprospector/product-research">product-research</a>'
    (SALES / "index.html").write_text(shell("aivp", "AI Value Prospectors — Sales materials", header, main, foot))


def build_brand(key, b):
    accent = b["cls"]  # 'pro' or 'edu'
    header = f'''    <header>
        <span class="wordmark"><span class="mark">{b['swatch']}</span><span class="name">{b['display']}</span></span>
        <h1>{b['display']} — Sales materials</h1>
        <p>{b['blurb']}</p>
        <a class="back" href="../index.html">&larr; All sales materials</a>
    </header>'''
    pages = "\n".join(page_card(href, b["swatch"], title, desc) for href, title, desc in b["pages"])
    dls = "\n".join(dl_card("../templates/", f, t, d, b["swatch"]) for f, t, d in b["downloads"])
    main = f'''        <p class="section-label"><span class="pip"></span>Reference pages <span class="hint">— read in the browser</span></p>
        <div class="card-grid">
{pages}
        </div>

        <p class="section-label"><span class="pip"></span>Downloadable templates <span class="hint">— make a copy, fill fields, export PDF</span></p>
        <div class="howto"><b>How to use:</b> download a file, drag it into Google Drive (it converts to a native Doc / Sheet / Slides), then <b>File → Make a copy</b>. Replace every <b>highlighted {{{{field}}}}</b> and <b>Download → PDF</b>.</div>
        <div class="card-grid">
{dls}
        </div>'''
    foot = f'{b["display"]} · {b["domain"]} · internal sales enablement · <a href="../index.html">All materials</a>'
    out = SALES / key / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(shell(accent, f"{b['display']} — Sales materials", header, main, foot))


def main():
    build_common()
    for key, b in BRANDS.items():
        build_brand(key, b)
    print("wrote sales/index.html, sales/proasiste/index.html, sales/eduasiste/index.html")


if __name__ == "__main__":
    main()
