"""Generate the luxury black+gold delivery PDFs for all three bundles.

The PDFs contain no reel URLs — the reel video files live in the same
Google Drive folder. Each PDF is the buyer's guide: what's inside the
vault and exactly how to use the reels on Instagram.

Re-run after any edits:
    python make_vault_pdf.py
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

BLACK = HexColor("#0a0a0c")
CARD = HexColor("#16161a")
GOLD = HexColor("#c9a227")
GOLD_BRIGHT = HexColor("#e8c65a")
TEXT = HexColor("#f2efe6")
MUTED = HexColor("#9b978c")

STORE = "Luxe Reels Vault"
IG_HANDLE = "@the.millionaire.frame"
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
W, H = A4

# ── The three bundles (mirror lib/products.js) ────────────────
BUNDLES = [
    {
        "file": "Starter-Vault-Access.pdf",
        "name": "Starter Vault",
        "sub": "50 Luxury Reels · Full HD · Watermark-free",
        "categories": [
            ("Supercars", 20),
            ("Luxury Watches", 15),
            ("High-End Lifestyle", 15),
        ],
        "bonus_lines": [],
    },
    {
        "file": "Creator-Pro-Vault-Access.pdf",
        "name": "Creator Pro Vault",
        "sub": "150 Luxury Reels · 4K + Full HD · Watermark-free",
        "categories": [
            ("Supercars", 30),
            ("Luxury Watches", 30),
            ("Private Jets & Yachts", 30),
            ("Real Estate & Interiors", 30),
            ("High-End Lifestyle & Fashion", 30),
        ],
        "bonus_lines": [
            "Your Bonus: 30 Viral Hook Captions",
            "Find the captions PDF in this same Google Drive folder.",
        ],
    },
    {
        "file": "Empire-Vault-Access.pdf",
        "name": "Empire Vault",
        "sub": "300+ Luxury Reels · 4K + Full HD · Watermark-free",
        "categories": [
            ("Supercars", 50),
            ("Luxury Watches", 50),
            ("Private Jets", 50),
            ("Yachts", 40),
            ("Real Estate & Interiors", 40),
            ("Fashion", 35),
            ("High-End Lifestyle", 35),
        ],
        "bonus_lines": [
            "Your Bonuses: 100 Hook Captions + Monetization Playbook",
            "Find both bonus PDFs in this same Google Drive folder.",
        ],
    },
]


def wrap(c, text, font, size, max_w):
    words = text.split()
    lines, cur = [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if c.stringWidth(trial, font, size) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def build_pdf(bundle):
    out = os.path.join(OUT_DIR, bundle["file"])
    c = canvas.Canvas(out, pagesize=A4)
    total_reels = sum(n for _, n in bundle["categories"])
    page = 0

    def bg():
        c.setFillColor(BLACK)
        c.rect(0, 0, W, H, stroke=0, fill=1)

    def gold_rule(y, x0=60, x1=W - 60):
        c.setStrokeColor(GOLD)
        c.setLineWidth(0.8)
        c.line(x0, y, x1, y)

    def footer():
        c.setFont("Helvetica", 8)
        c.setFillColor(MUTED)
        c.drawCentredString(W / 2, 34, f"{STORE}  ·  {bundle['name']}  ·  Page {page}")

    def content_page(title_text):
        nonlocal page
        page += 1
        bg()
        c.setFillColor(GOLD_BRIGHT)
        c.setFont("Times-Bold", 20)
        c.drawString(60, H - 70, bundle["name"])
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 9)
        c.drawRightString(W - 60, H - 68, title_text)
        gold_rule(H - 84)
        return H - 130

    def section(y, heading):
        c.setFillColor(GOLD)
        c.setFont("Helvetica-Bold", 13)
        c.drawString(60, y, heading.upper())
        return y - 24

    def body(y, text, indent=60):
        c.setFillColor(TEXT)
        c.setFont("Helvetica", 10.5)
        for line in wrap(c, text, "Helvetica", 10.5, W - indent - 60):
            c.drawString(indent, y, line)
            y -= 15
        return y - 6

    def bullet(y, text):
        c.setFillColor(GOLD_BRIGHT)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(66, y, "✦"[0] if False else "-")
        c.setFillColor(TEXT)
        c.setFont("Helvetica", 10.5)
        for i, line in enumerate(wrap(c, text, "Helvetica", 10.5, W - 82 - 60)):
            c.drawString(82, y - i * 15, line)
            y -= 15
        return y - 4

    # ── Cover ─────────────────────────────────────────────────
    page += 1
    bg()
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.2)
    c.rect(40, 40, W - 80, H - 80, stroke=1, fill=0)
    c.setLineWidth(0.5)
    c.rect(48, 48, W - 96, H - 96, stroke=1, fill=0)

    c.setFillColor(GOLD_BRIGHT)
    c.setFont("Helvetica", 11)
    c.drawCentredString(W / 2, H - 200, "*   P R E M I U M   C O N T E N T   V A U L T   *")

    c.setFillColor(TEXT)
    c.setFont("Times-Bold", 44)
    c.drawCentredString(W / 2, H - 300, bundle["name"])

    c.setFillColor(GOLD_BRIGHT)
    c.setFont("Times-Italic", 16)
    c.drawCentredString(W / 2, H - 335, bundle["sub"])

    gold_rule(H - 380, W / 2 - 90, W / 2 + 90)

    c.setFillColor(MUTED)
    c.setFont("Helvetica", 11)
    c.drawCentredString(W / 2, H - 430, "Thank you for your purchase.")
    c.drawCentredString(W / 2, H - 448, "All your reel files are in this Google Drive folder, organised by niche.")
    c.drawCentredString(W / 2, H - 466, "This guide shows you exactly how to use them to grow your page.")

    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8)
    c.drawCentredString(W / 2, 120, f"© 2026 {STORE} · For the buyer's use only · Please do not reshare this folder or document")
    c.showPage()

    # ── Page: What's inside ───────────────────────────────────
    y = content_page("What's Inside")
    y = section(y, "Your vault at a glance")
    y = body(y, f"Your {bundle['name']} contains {total_reels} watermark-free luxury reels, organised into folders by niche:")
    y -= 6
    for cat, count in bundle["categories"]:
        if y < 90:
            footer(); c.showPage(); y = content_page("What's Inside")
        c.setFillColor(CARD)
        c.rect(55, y - 6, W - 110, 22, stroke=0, fill=1)
        c.setFillColor(GOLD_BRIGHT)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(66, y, cat)
        c.setFillColor(TEXT)
        c.setFont("Helvetica", 10)
        c.drawRightString(W - 66, y, f"{count} reels")
        y -= 28
    y -= 8
    y = section(y, "How to download")
    y = bullet(y, "On phone: open the Drive folder, tap the three dots on any reel, then 'Download'. To grab a whole niche at once, use the Google Drive app and long-press the folder.")
    y = bullet(y, "On computer: select multiple files (Ctrl/Cmd-click), right-click, 'Download' — Drive zips them for you. Transfer to your phone via AirDrop, cable, or your own Drive.")
    y = bullet(y, "Save this folder to 'Starred' in Drive so you can always find it again.")
    footer()
    c.showPage()

    # ── Page: How to post on Instagram ────────────────────────
    y = content_page("Posting Guide")
    y = section(y, "The 5-step posting routine")
    y = bullet(y, "1. Pick one reel from the niche that fits your page's theme today. Don't post the same niche twice in a row — variety keeps the feed fresh.")
    y = bullet(y, "2. Open Instagram, create a new Reel, and add the video from your camera roll.")
    y = bullet(y, "3. Add trending audio: tap the music icon and pick a sound marked with the trending arrow. Keep the original video muted if the sound clashes.")
    y = bullet(y, "4. Add a hook as on-screen text in the first 2 seconds" + (" — use your bonus captions pack in this folder." if bundle["bonus_lines"] else " — a short bold line that stops the scroll."))
    y = bullet(y, "5. Write the caption: hook line first, one line of value or story, then a CTA ('Save this', 'Follow for daily luxury', 'Comment KEYS'). Add 3-5 niche hashtags, not 30.")
    y -= 8
    y = section(y, "When and how often")
    y = bullet(y, "Post 1-2 reels per day, every day. Consistency beats perfection — the algorithm rewards accounts that show up daily.")
    y = bullet(y, "Best windows (IST): 11 AM - 1 PM and 7 PM - 10 PM. Test both for two weeks and check Insights to find YOUR audience's peak.")
    y = bullet(y, "Spend the first 30 minutes after posting replying to every comment — early engagement tells Instagram to push the reel further.")
    footer()
    c.showPage()

    # ── Page: Do's & Don'ts ───────────────────────────────────
    y = content_page("Do's & Don'ts")
    y = section(y, "Do")
    y = bullet(y, "Build ONE clear theme — a luxury page, a motivation page, a watches page. Pages with a clear identity grow far faster than mixed feeds.")
    y = bullet(y, "Batch your work: download 10 reels on Sunday, pick their audios and captions, and schedule your whole week in one sitting.")
    y = bullet(y, "Watch your Insights weekly. Double down on the niche that gets the most reach on YOUR page.")
    y = bullet(y, "Combine reels with Stories: repost your own reel to your Story with a poll or question sticker for extra reach.")
    y -= 8
    y = section(y, "Don't")
    y = bullet(y, "Don't reshare this Drive folder or PDF — access is licensed to you only, and shared links get revoked.")
    y = bullet(y, "Don't post 10 reels in one day then vanish for a week. The algorithm punishes inconsistency.")
    y = bullet(y, "Don't delete underperforming reels — some pick up reach days later.")
    y = bullet(y, "Don't buy followers or use engagement pods. They wreck your reach permanently.")
    footer()
    c.showPage()

    # ── Support / bonus page ──────────────────────────────────
    page += 1
    bg()
    top_y = H - 120
    heading = bundle["bonus_lines"][0] if bundle["bonus_lines"] else "Enjoy Your Vault"
    c.setFillColor(GOLD_BRIGHT)
    c.setFont("Times-Bold", 22)
    c.drawCentredString(W / 2, top_y, heading)
    gold_rule(top_y - 20, W / 2 - 140, W / 2 + 140)
    if bundle["bonus_lines"]:
        c.setFillColor(TEXT)
        c.setFont("Helvetica", 10)
        c.drawCentredString(W / 2, top_y - 55, bundle["bonus_lines"][1])

    c.setFillColor(CARD)
    c.roundRect(100, H - 420, W - 200, 180, 10, stroke=0, fill=1)
    c.setStrokeColor(GOLD)
    c.roundRect(100, H - 420, W - 200, 180, 10, stroke=1, fill=0)
    c.setFillColor(GOLD_BRIGHT)
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(W / 2, H - 275, "NEED HELP?")
    c.setFillColor(TEXT)
    c.setFont("Helvetica", 10)
    for i, line in enumerate([
        "A file not opening, or a reel missing?  DM us on Instagram",
        "with your Payment ID — we'll fix it within 24 hours.",
        "",
        f"Instagram:  {IG_HANDLE}",
    ]):
        c.drawCentredString(W / 2, H - 305 - i * 20, line)

    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8)
    c.drawCentredString(W / 2, 60, f"© 2026 {STORE} · Thank you for building your empire with us")
    footer()
    c.showPage()

    c.save()
    print(f"Created: {bundle['file']}  ({page} pages, {total_reels} reels)")


for b in BUNDLES:
    build_pdf(b)
