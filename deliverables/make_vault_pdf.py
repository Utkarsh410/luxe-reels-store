"""Generate the luxury black+gold delivery PDF for a reels bundle.

Edit REELS below (or pass a different bundle config) and re-run:
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

BUNDLE_NAME = "Creator Pro Vault"
BUNDLE_SUB = "150 Luxury Reels Â· 4K + Full HD Â· Watermark-free"
STORE = "Luxe Reels Vault"

# â”€â”€ Replace these with your real reel download links â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
CATEGORIES = [
    ("Supercars", 30),
    ("Luxury Watches", 30),
    ("Private Jets & Yachts", 30),
    ("Real Estate & Interiors", 30),
    ("High-End Lifestyle & Fashion", 30),
]
def link_placeholder(cat, i):
    return f"https://drive.google.com/REPLACE_reel_{cat.split()[0].lower()}_{i:02d}"

W, H = A4
OUT = os.path.join(r"C:\Users\AUM\luxe-reels-store", "deliverables", "Creator-Pro-Vault-Access.pdf")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

c = canvas.Canvas(OUT, pagesize=A4)


def bg():
    c.setFillColor(BLACK)
    c.rect(0, 0, W, H, stroke=0, fill=1)


def gold_rule(y, x0=60, x1=W - 60):
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.8)
    c.line(x0, y, x1, y)


def footer(page_num):
    c.setFont("Helvetica", 8)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 34, f"{STORE}  Â·  {BUNDLE_NAME}  Â·  Page {page_num}")


# â”€â”€ Cover page â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
bg()
c.setStrokeColor(GOLD)
c.setLineWidth(1.2)
c.rect(40, 40, W - 80, H - 80, stroke=1, fill=0)
c.setLineWidth(0.5)
c.rect(48, 48, W - 96, H - 96, stroke=1, fill=0)

c.setFillColor(GOLD_BRIGHT)
c.setFont("Helvetica", 11)
c.drawCentredString(W / 2, H - 200, "âœ¦   P R E M I U M   C O N T E N T   V A U L T   âœ¦".replace("âœ¦", "*"))

c.setFillColor(TEXT)
c.setFont("Times-Bold", 44)
c.drawCentredString(W / 2, H - 300, "Creator Pro Vault")

c.setFillColor(GOLD_BRIGHT)
c.setFont("Times-Italic", 16)
c.drawCentredString(W / 2, H - 335, BUNDLE_SUB)

gold_rule(H - 380, W / 2 - 90, W / 2 + 90)

c.setFillColor(MUTED)
c.setFont("Helvetica", 11)
c.drawCentredString(W / 2, H - 430, "Thank you for your purchase.")
c.drawCentredString(W / 2, H - 448, "This document contains download links for every reel in your bundle.")

c.setFillColor(CARD)
c.roundRect(100, 180, W - 200, 130, 10, stroke=0, fill=1)
c.setStrokeColor(GOLD)
c.roundRect(100, 180, W - 200, 130, 10, stroke=1, fill=0)
c.setFillColor(GOLD_BRIGHT)
c.setFont("Helvetica-Bold", 12)
c.drawCentredString(W / 2, 280, "HOW TO USE")
c.setFillColor(TEXT)
c.setFont("Helvetica", 10)
for i, line in enumerate([
    "1.  Click any link below (or copy it into your browser) to download the reel.",
    "2.  Post directly to your Instagram page â€” all reels are watermark-free.",
    "3.  Pair with trending audio and the hook captions included in your bundle.",
]):
    c.drawString(130, 254 - i * 22, line)

c.setFillColor(MUTED)
c.setFont("Helvetica", 8)
c.drawCentredString(W / 2, 120, f"Â© 2026 {STORE} Â· For the buyer's use only Â· Please do not reshare this document")
c.showPage()

# â”€â”€ Link pages â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
page = 2
reel_no = 0
y = 0

def new_page(cat=None):
    global y
    bg()
    c.setFillColor(GOLD_BRIGHT)
    c.setFont("Times-Bold", 20)
    c.drawString(60, H - 70, BUNDLE_NAME)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 9)
    c.drawRightString(W - 60, H - 68, "Reel Download Links")
    gold_rule(H - 84)
    y = H - 120

for cat, count in CATEGORIES:
    new_page()
    # Category header
    c.setFillColor(GOLD)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(60, y, cat.upper())
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 9)
    c.drawRightString(W - 60, y, f"{count} reels")
    y -= 26

    for i in range(1, count + 1):
        reel_no += 1
        if y < 70:
            footer(page)
            c.showPage()
            page += 1
            new_page()
        # Row
        if i % 2 == 1:
            c.setFillColor(CARD)
            c.rect(55, y - 6, W - 110, 20, stroke=0, fill=1)
        c.setFillColor(GOLD_BRIGHT)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(64, y, f"{reel_no:03d}")
        c.setFillColor(TEXT)
        c.setFont("Helvetica", 9)
        c.drawString(95, y, f"{cat} Reel {i:02d}")
        url = link_placeholder(cat, i)
        c.setFillColor(GOLD)
        c.setFont("Helvetica", 8)
        shown = url if len(url) <= 60 else url[:57] + "..."
        c.drawRightString(W - 64, y, shown)
        c.linkURL(url, (55, y - 6, W - 55, y + 14), relative=0)
        y -= 21

    footer(page)
    c.showPage()
    page += 1

# â”€â”€ Bonus / support page â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
bg()
c.setFillColor(GOLD_BRIGHT)
c.setFont("Times-Bold", 24)
c.drawCentredString(W / 2, H - 120, "Bonus: 30 Viral Hook Captions")
gold_rule(H - 140, W / 2 - 120, W / 2 + 120)
c.setFillColor(TEXT)
c.setFont("Helvetica", 10)
c.drawCentredString(W / 2, H - 175, "Find your bonus captions file in the same Google Drive folder as this PDF.")

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
    "A link not working?  DM us on Instagram with your Payment ID",
    "and the reel number â€” we'll fix it within 24 hours.",
    "",
    "Instagram:  @the.millionaire.frame",
]):
    c.drawCentredString(W / 2, H - 305 - i * 20, line)

c.setFillColor(MUTED)
c.setFont("Helvetica", 8)
c.drawCentredString(W / 2, 60, f"Â© 2026 {STORE} Â· Thank you for building your empire with us")
footer(page)
c.showPage()

c.save()
print(f"Created: {OUT}  ({page} pages)")
