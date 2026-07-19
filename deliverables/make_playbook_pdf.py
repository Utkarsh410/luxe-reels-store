"""Generate the 'Monetization Playbook' bonus PDF (Empire Vault) in the
Luxe Reels Vault black+gold style.

Re-run after any edits:
    python make_playbook_pdf.py
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
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Bonus-Monetization-Playbook.pdf")
W, H = A4

c = canvas.Canvas(OUT, pagesize=A4)
page = 0


def wrap(text, font, size, max_w):
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
    c.drawCentredString(W / 2, 34, f"{STORE}  ·  Monetization Playbook  ·  Page {page}")


def content_page(corner):
    global page
    page += 1
    bg()
    c.setFillColor(GOLD_BRIGHT)
    c.setFont("Times-Bold", 20)
    c.drawString(60, H - 70, "Monetization Playbook")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 9)
    c.drawRightString(W - 60, H - 68, corner)
    gold_rule(H - 84)
    return H - 130


def section(y, heading):
    c.setFillColor(GOLD)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(60, y, heading.upper())
    return y - 24


def body(y, text):
    c.setFillColor(TEXT)
    c.setFont("Helvetica", 10.5)
    for line in wrap(text, "Helvetica", 10.5, W - 120):
        c.drawString(60, y, line)
        y -= 15
    return y - 6


def bullet(y, text):
    c.setFillColor(GOLD_BRIGHT)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(66, y, "-")
    c.setFillColor(TEXT)
    c.setFont("Helvetica", 10.5)
    for i, line in enumerate(wrap(text, "Helvetica", 10.5, W - 142)):
        c.drawString(82, y - i * 15, line)
        y -= 15
    return y - 4


# ── Cover ─────────────────────────────────────────────────────
page += 1
bg()
c.setStrokeColor(GOLD)
c.setLineWidth(1.2)
c.rect(40, 40, W - 80, H - 80, stroke=1, fill=0)
c.setLineWidth(0.5)
c.rect(48, 48, W - 96, H - 96, stroke=1, fill=0)

c.setFillColor(GOLD_BRIGHT)
c.setFont("Helvetica", 11)
c.drawCentredString(W / 2, H - 200, "*   E M P I R E   V A U L T   B O N U S   *")

c.setFillColor(TEXT)
c.setFont("Times-Bold", 42)
c.drawCentredString(W / 2, H - 295, "Monetization Playbook")

c.setFillColor(GOLD_BRIGHT)
c.setFont("Times-Italic", 15)
c.drawCentredString(W / 2, H - 330, "Turn a luxury theme page into an income stream")

gold_rule(H - 375, W / 2 - 90, W / 2 + 90)

c.setFillColor(MUTED)
c.setFont("Helvetica", 11)
c.drawCentredString(W / 2, H - 430, "The exact ladder: post daily → grow an audience → get paid.")
c.drawCentredString(W / 2, H - 448, "No fluff. Follow it phase by phase.")

c.setFillColor(MUTED)
c.setFont("Helvetica", 8)
c.drawCentredString(W / 2, 120, f"© 2026 {STORE} · For the buyer's use only · Please do not reshare this document")
c.showPage()

# ── Phase 1: Foundation ───────────────────────────────────────
y = content_page("Phase 1 · 0 - 1,000 followers")
y = section(y, "Phase 1 — Build the machine")
y = body(y, "Nobody pays a page without an identity. Before chasing money, make the page worth paying.")
y = bullet(y, "Pick ONE angle for your page: pure luxury visuals, money motivation, or a single niche like watches. Write it in your bio in plain words, e.g. 'Daily luxury & mindset'.")
y = bullet(y, "Handle and name: short, readable, no numbers if possible. The name field is searchable — include a keyword like 'Luxury' or 'Wealth'.")
y = bullet(y, "Profile photo: a clean gold-on-black monogram or logo. Consistency across posts makes the page look established from day one.")
y = bullet(y, "Switch to a Professional account (free) so you can see Insights.")
y = bullet(y, "Post 1-2 reels daily from your vault using the posting routine in your vault guide. Batch on Sundays.")
y = bullet(y, "Set up 3 Story highlights: 'Start Here' (what the page is), 'Best Reels', and later 'Shop'.")
y -= 8
y = section(y, "Phase 1 goal")
y = body(y, "1,000 followers and a consistent 30-day posting streak. Don't try to monetize before this — you'll waste the audience's trust for pennies.")
footer()
c.showPage()

# ── Phase 2: Growth ───────────────────────────────────────────
y = content_page("Phase 2 · 1,000 - 10,000 followers")
y = section(y, "Phase 2 — Pour fuel on what works")
y = bullet(y, "Check Insights weekly. Find your top 3 reels by reach — post more of that exact niche and audio style.")
y = bullet(y, "Reply to every comment within 30 minutes of posting. Comments are the strongest growth signal Instagram reads.")
y = bullet(y, "Use CTAs that create comments: 'Comment KEYS if this is the goal' out-performs 'like and share' every time.")
y = bullet(y, "Collaborate: find 5 pages your size in the same niche, exchange shares or use Instagram's Collab feature on a post — both audiences see it.")
y = bullet(y, "Stories daily: repost your reel, add a poll or 'this or that' sticker. Story viewers are your most loyal followers — they're the ones who buy later.")
y -= 8
y = section(y, "Phase 2 goal")
y = body(y, "10,000 followers with 3-5% engagement. At this size, monetization stops being theoretical.")
footer()
c.showPage()

# ── Phase 3: Monetization streams ─────────────────────────────
y = content_page("Phase 3 · The income streams")
y = section(y, "Stream 1 — Shoutouts & promotions")
y = body(y, "Other pages and small brands pay theme pages to post their content or mention them. Typical Indian market rates: roughly Rs 300-800 per promo at 10k followers, Rs 1,500-5,000 at 50k, and Rs 5,000-15,000+ at 100k with good engagement.")
y = bullet(y, "Put 'DM for promotions' in your bio once you cross ~10k.")
y = bullet(y, "Only promote things that fit the theme — one bad promo costs more trust than ten good ones earn.")
y -= 8
y = section(y, "Stream 2 — Affiliate income")
y = bullet(y, "Join affiliate programs that match luxury/self-improvement: Amazon Associates (watches, books, gadgets), trading & finance apps, courses.")
y = bullet(y, "Put the affiliate link in your bio link page and mention it in captions: 'Gear I recommend — link in bio'.")
y = bullet(y, "Story link stickers are your best affiliate tool — one swipe from an interested viewer.")
y -= 8
y = section(y, "Stream 3 — Sell your own digital product")
y = bullet(y, "The biggest margin: your own product. Ebooks, preset packs, guides — or content bundles like the one you bought.")
y = bullet(y, "Create it once, deliver it automatically, price it Rs 299-1,999. Ten sales a week at Rs 999 is Rs 40,000/month.")
y = bullet(y, "Use a simple store with instant delivery so it runs while you sleep.")
footer()
c.showPage()

# ── Phase 3 continued + math ──────────────────────────────────
y = content_page("Phase 3 · continued")
y = section(y, "Stream 4 — Brand deals")
y = body(y, "Past 50k followers, real brands (watch retailers, fashion labels, fintech apps) reach out or respond to pitches. A media kit — one page with your niche, reach, engagement rate and audience age/location from Insights — doubles your close rate.")
y -= 8
y = section(y, "Stream 5 — Page flipping (advanced)")
y = body(y, "Grown theme pages sell. A well-run 100k luxury page can sell for serious money. Build one page to sustain income first; only then consider growing pages to sell.")
y -= 8
y = section(y, "The realistic math")
y = bullet(y, "Month 1-3: Rs 0. You're building. Anyone promising instant money is lying.")
y = bullet(y, "Month 4-6 (10-25k followers): Rs 3,000-10,000/month from shoutouts + affiliates.")
y = bullet(y, "Month 7-12 (25-75k): Rs 10,000-40,000/month adding your own product.")
y = bullet(y, "Year 2 (100k+): Rs 50,000+/month across all five streams is achievable with consistency.")
y = body(y, "These are typical ranges for consistent pages, not guarantees — your niche, engagement and effort decide where you land.")
footer()
c.showPage()

# ── Mistakes ──────────────────────────────────────────────────
y = content_page("Avoid these")
y = section(y, "The 7 mistakes that kill theme pages")
y = bullet(y, "1. Monetizing too early. Promos at 2k followers make the page look desperate and stall growth.")
y = bullet(y, "2. Inconsistency. Three weeks daily, then silence. The algorithm forgets you in days.")
y = bullet(y, "3. Mixed themes. Luxury cars today, memes tomorrow. Confused followers don't convert.")
y = bullet(y, "4. Buying followers. Dead weight that destroys your reach ratio forever.")
y = bullet(y, "5. Ignoring Stories and comments. Reels bring strangers; conversation turns them into buyers.")
y = bullet(y, "6. Promoting junk. Every promo is a withdrawal from your trust account. Spend carefully.")
y = bullet(y, "7. Quitting at month two. The compounding starts exactly where most people stop.")
footer()
c.showPage()

# ── Support ───────────────────────────────────────────────────
page += 1
bg()
c.setFillColor(GOLD_BRIGHT)
c.setFont("Times-Bold", 24)
c.drawCentredString(W / 2, H - 120, "Now Go Build")
gold_rule(H - 140, W / 2 - 120, W / 2 + 120)
c.setFillColor(TEXT)
c.setFont("Helvetica", 10)
c.drawCentredString(W / 2, H - 175, "You have 300+ reels, 100 hooks, and the roadmap.")
c.drawCentredString(W / 2, H - 192, "The only variable left is how many days in a row you show up.")

c.setFillColor(CARD)
c.roundRect(100, H - 420, W - 200, 160, 10, stroke=0, fill=1)
c.setStrokeColor(GOLD)
c.roundRect(100, H - 420, W - 200, 160, 10, stroke=1, fill=0)
c.setFillColor(GOLD_BRIGHT)
c.setFont("Helvetica-Bold", 12)
c.drawCentredString(W / 2, H - 295, "QUESTIONS?")
c.setFillColor(TEXT)
c.setFont("Helvetica", 10)
c.drawCentredString(W / 2, H - 325, f"DM us on Instagram:  {IG_HANDLE}")

c.setFillColor(MUTED)
c.setFont("Helvetica", 8)
c.drawCentredString(W / 2, 60, f"© 2026 {STORE} · Thank you for building your empire with us")
footer()
c.showPage()

c.save()
print(f"Created: Bonus-Monetization-Playbook.pdf  ({page} pages)")
