#!/usr/bin/env python3
"""Generate ../sales/templates.html — a branded download index of the en/ templates."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
OUT = REPO / "sales" / "templates.html"
PUBLISH = REPO / "sales" / "templates"  # files served directly under /sales/templates/

FMT = {"docx": ("Doc", "Google Docs"), "xlsx": ("Sheet", "Google Sheets"),
       "pptx": ("Slides", "Google Slides")}

# slug -> (title, description). Order within each group matters.
META = {
    # cross / AIVP
    "aivp-one-pager": ("One-Pager — How Two Twins Work Together", "Both-brands leave-behind: EduAsiste + ProAsiste day-one pillars, with a rep contact line. Export to PDF."),
    "aivp-pitch-deck": ("Pitch Deck — Two Twins", "~8-slide cross-brand deck with speaker notes; family + business examples side by side. Editable skeleton."),
    "aivp-email-templates": ("Cross-Twin Email Templates", "Five outreach emails (education + business leaning) plus tips. Fill the highlighted fields and send."),
    "knowledge-demo-guide": ("Knowledge Demo Guide", "Tab-by-tab platform demo script (Import · View · Task · Verify) — works for both brands."),
    "aivp-pricing-roi-calculator": ("Pricing & ROI Calculator", "Live Sheet: pick tier + seats + billing, see Year-1 and ongoing cost with the certification-waiver math."),
    "aivp-pipeline-tracker": ("Sales Pipeline Tracker", "Shared Sheet: Prospect → Pro → Member stages, auto est. value per row, pipeline summary."),
    # ProAsiste
    "proasiste-one-pager": ("ProAsiste One-Pager", "Business leave-behind: owner-twin + team-twin pillars. Print/PDF ready."),
    "proasiste-pitch-deck": ("ProAsiste Pitch Deck", "~8-slide business deck with speaker notes. Editable skeleton."),
    "proasiste-email-templates": ("ProAsiste Email Templates", "Business outreach by angle (time-saver, competitor, knowledge-loss). Highlighted fill-in fields."),
    "proasiste-quick-reference": ("ProAsiste Quick Reference Card", "One-page cheat sheet: pitch, tabs, pain→response, tiers. Print-friendly."),
    "proasiste-competitive": ("ProAsiste Competitive Positioning", "Battle cards vs. ChatGPT / Copilot. Their argument, your response, differentiator tables."),
    "proasiste-security-faq": ("ProAsiste Security FAQ", "Tier × infrastructure security, what's included, KloudStax compliance path."),
    "proasiste-personas": ("ProAsiste Customer Personas", "Business buyer profiles with pains, demo focus, and closing language."),
    "proasiste-pricing-roi-calculator": ("ProAsiste Pricing & ROI Calculator", "Live Sheet: tier/seats/billing → Year-1 + ongoing cost, certification-waiver math."),
    # EduAsiste
    "eduasiste-one-pager": ("EduAsiste One-Pager", "Education leave-behind: parent-twin + child-twin pillars. Print/PDF ready."),
    "eduasiste-pitch-deck": ("EduAsiste Pitch Deck", "~8-slide education deck with speaker notes. Editable skeleton."),
    "eduasiste-email-templates": ("EduAsiste Email Templates", "Parent / tutor / school outreach. Highlighted fill-in fields."),
    "eduasiste-quick-reference": ("EduAsiste Quick Reference Card", "One-page cheat sheet for parent/school calls. Print-friendly."),
    "eduasiste-competitive": ("EduAsiste Competitive Positioning", "Battle cards vs. generic AI, grade portals, content libraries, tutoring."),
    "eduasiste-security-faq": ("EduAsiste Security FAQ", "FERPA / COPPA / GDPR, minors' data, transparency pillar. KloudStax for formal frameworks."),
    "eduasiste-personas": ("EduAsiste Customer Personas", "Five education buyer profiles: involved parent, homeschool, tutor, school admin, achievement-focused."),
    "eduasiste-pricing-roi-calculator": ("EduAsiste Pricing & ROI Calculator", "Live Sheet: tier/seats/billing → Year-1 + ongoing cost, certification-waiver math."),
}

GROUPS = [
    ("cross", "Cross-Twin &amp; platform", "both brands", "↔",
     ["aivp-one-pager", "aivp-pitch-deck", "aivp-email-templates", "knowledge-demo-guide",
      "aivp-pricing-roi-calculator", "aivp-pipeline-tracker"]),
    ("pro", "ProAsiste", "business · proasiste.com", "Pro",
     ["proasiste-one-pager", "proasiste-pitch-deck", "proasiste-email-templates",
      "proasiste-quick-reference", "proasiste-competitive", "proasiste-security-faq",
      "proasiste-personas", "proasiste-pricing-roi-calculator"]),
    ("edu", "EduAsiste", "education · eduasiste.org", "Edu",
     ["eduasiste-one-pager", "eduasiste-pitch-deck", "eduasiste-email-templates",
      "eduasiste-quick-reference", "eduasiste-competitive", "eduasiste-security-faq",
      "eduasiste-personas", "eduasiste-pricing-roi-calculator"]),
]


def card(slug, edu):
    f = None
    for ext in ("docx", "xlsx", "pptx"):
        if (HERE / "en" / f"{slug}.{ext}").exists():
            f = f"{slug}.{ext}"; break
    if not f:
        return ""
    ext = f.rsplit(".", 1)[1]
    badge, native = FMT[ext]
    title, desc = META[slug]
    cls = "card edu" if edu else "card"
    return f'''            <a class="{cls}" href="templates/{f}" download>
                <div class="swatch">{badge}</div>
                <h2>{title}</h2>
                <div class="desc">{desc}</div>
                <div class="meta">Downloads <code>{f}</code> → opens in {native}</div>
            </a>'''


def main():
    sections = []
    n = 0
    for key, label, hint, _pip, slugs in GROUPS:
        cards = "\n".join(c for c in (card(s, key == "edu") for s in slugs) if c)
        n += sum(1 for s in slugs if (HERE / "en").glob(f"{s}.*"))
        edu = " edu" if key == "edu" else ""
        sections.append(
            f'        <p class="section-label{edu}"><span class="pip"></span>{label} '
            f'<span class="hint">— {hint}</span></p>\n'
            f'        <div class="card-grid">\n{cards}\n        </div>')
    body = "\n\n".join(sections)
    html = TEMPLATE.replace("{{SECTIONS}}", body)
    OUT.write_text(html)
    # publish the built files into /sales/templates/ for direct download
    import shutil
    PUBLISH.mkdir(exist_ok=True)
    copied = 0
    for f in sorted((HERE / "en").glob("*")):
        if f.suffix in (".docx", ".xlsx", ".pptx"):
            shutil.copy2(f, PUBLISH / f.name)
            copied += 1
    print(f"wrote {OUT} ({len(META)} templates); published {copied} files to {PUBLISH}")


TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
    <meta name="robots" content="noindex, nofollow">
    <title>AI Value Prospectors — Copy-and-customize templates</title>
    <style>
        :root{--aivp:#E8B547;--aivp-dark:#92700f;--edu:#2EA3F2;--edu-dark:#1d6fb0;
        --bg:#0F1115;--card-bg:#181B22;--text:#F3F4F6;--text-soft:#C2C6CC;--muted:#9AA0A6;--border:#2A2E37;}
        *{box-sizing:border-box;}
        body{margin:0;font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;background:var(--bg);color:var(--text);min-height:100vh;display:flex;flex-direction:column;}
        header{padding:40px 24px 16px;text-align:center;border-bottom:1px solid var(--border);}
        .wordmark{display:inline-flex;align-items:center;gap:10px;margin-bottom:12px;}
        .wordmark .mark{width:38px;height:38px;border-radius:9px;background:var(--aivp);color:#0F1115;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:18px;letter-spacing:-0.03em;}
        .wordmark .name{font-size:15px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:var(--aivp);}
        header h1{margin:0;font-size:30px;font-weight:800;letter-spacing:-0.02em;}
        header p{margin:10px auto 0;color:var(--muted);font-size:15px;max-width:620px;}
        header a.back{display:inline-block;margin-top:14px;color:var(--text-soft);text-decoration:none;font-size:13px;font-weight:600;}
        header a.back:hover{color:var(--aivp);}
        main{flex:1;max-width:1040px;margin:0 auto;padding:24px;width:100%;}
        .howto{background:var(--card-bg);border:1px solid var(--border);border-left:3px solid var(--aivp);border-radius:12px;padding:18px 22px;margin:8px 0 8px;font-size:14px;color:var(--text-soft);line-height:1.6;}
        .howto b{color:var(--text);}
        .section-label{font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:0.06em;color:var(--text-soft);margin:30px 0 0;display:flex;align-items:center;gap:10px;}
        .section-label .pip{width:10px;height:10px;border-radius:50%;background:var(--aivp);}
        .section-label.edu .pip{background:var(--edu);}
        .section-label .hint{font-weight:500;text-transform:none;letter-spacing:0;color:var(--muted);font-size:13px;}
        .card-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px;margin-top:16px;}
        .card{background:var(--card-bg);border:1px solid var(--border);border-radius:14px;padding:22px;text-decoration:none;color:inherit;display:flex;flex-direction:column;gap:8px;transition:transform 120ms,box-shadow 120ms,border-color 120ms;}
        .card:hover{transform:translateY(-2px);box-shadow:0 10px 28px rgba(0,0,0,.35);border-color:var(--aivp);}
        .card.edu:hover{border-color:var(--edu);}
        .card .swatch{align-self:flex-start;padding:4px 10px;border-radius:8px;background:var(--aivp);color:#0F1115;font-size:12px;font-weight:800;letter-spacing:.02em;}
        .card.edu .swatch{background:var(--edu);color:#06243b;}
        .card h2{margin:0;font-size:17px;font-weight:700;}
        .card .desc{color:var(--text-soft);font-size:13.5px;line-height:1.55;}
        .card .meta{margin-top:auto;padding-top:12px;font-size:12px;color:var(--muted);}
        .card .meta code{font-family:ui-monospace,Menlo,monospace;color:var(--text-soft);}
        footer{text-align:center;color:var(--muted);font-size:13px;padding:28px 24px;border-top:1px solid var(--border);}
        footer a{color:var(--aivp);text-decoration:none;}
    </style>
</head>
<body>
    <header>
        <span class="wordmark"><span class="mark">Ai</span><span class="name">AI Value Prospectors</span></span>
        <h1>Copy-and-customize templates</h1>
        <p>Branded Google Docs, Sheets &amp; Slides templates — open one, make a copy, fill the highlighted fields, export to PDF.</p>
        <a class="back" href="index.html">&larr; Back to sales materials</a>
    </header>
    <main>
        <div class="howto">
            <b>How to use:</b> download a file below, drag it into Google Drive (it converts to a native Google Doc / Sheet / Slides), then <b>File → Make a copy</b> for each prospect. Replace every <b>highlighted {{field}}</b>, then <b>File → Download → PDF</b> to send. A shared Drive folder with one-click “Make a copy” links is coming next.
        </div>

{{SECTIONS}}

    </main>
    <footer>AI Value Prospectors · internal sales enablement · Source: <a href="https://github.com/aivalueprospector/product-research">product-research</a> #31</footer>
</body>
</html>
'''


if __name__ == "__main__":
    main()
