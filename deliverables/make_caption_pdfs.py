"""Generate the bonus 'Viral Hook Captions' PDFs (30-pack for Creator Pro,
100-pack for Empire) in the Luxe Reels Vault black+gold style.

Re-run after any edits:
    python make_caption_pdfs.py
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

# ── The captions, grouped by niche ────────────────────────────
CAPTIONS = {
    "Supercars": [
        "POV: You stopped explaining your dreams to people who drive rentals.",
        "This isn't a car. It's proof that 'impossible' was a lie.",
        "They laughed at the vision board. The V12 laughed back.",
        "Rule #1: Never ask the price. Ask how many.",
        "Alarm at 5AM sounds different when this is in the garage.",
        "Some chase weekends. Others chase horsepower.",
        "The quietest man in the room owns the loudest engine.",
        "Traffic doesn't exist at 300 km/h.",
        "You don't buy this car. You become the person who owns it first.",
        "Fuel is expensive. Regret is more.",
        "0 to 100 in 2.9s — faster than they changed their opinion of you.",
        "Garage goals aren't luck. They're invoices paid by discipline.",
        "Every scratch on a rental. Never on a dream.",
        "The test drive they never let you forget.",
        "Built different isn't a caption. It's a spec sheet.",
    ],
    "Luxury Watches": [
        "A watch doesn't tell time. It tells people who you are.",
        "He checked his wrist. The room checked theirs.",
        "Old money whispers. This wrist doesn't need to speak at all.",
        "Time is the only thing you can't buy back. Wear it well.",
        "Waitlists exist so the patient can beat the rich.",
        "Your grandfather's advice, your future son's inheritance.",
        "It's not about the hours. It's about what you did with them.",
        "Steel appreciates. Excuses don't.",
        "The meeting starts when this wrist enters the room.",
        "Some wear watches. Some wear milestones.",
        "Complications on the dial. None in the bank account.",
        "A quiet flex ticks 28,800 times a day.",
        "First you earn the watch. Then the watch earns the room.",
        "Legacy is measured in millimeters of sapphire.",
        "Five figures on the wrist, six lessons behind it.",
    ],
    "Private Jets & Yachts": [
        "Boarding pass? Never heard of her.",
        "The layover is wherever I say it is.",
        "Security line: skipped. Standards: never.",
        "Altitude changes attitude.",
        "Some sail through life. Literally.",
        "International waters, domestic peace.",
        "The ocean doesn't care about your job title. The marina does.",
        "Wheels up at 9. Excuses grounded forever.",
        "First class was the goal. Then the goalpost moved.",
        "Sunsets hit different from the upper deck.",
    ],
    "Real Estate & Interiors": [
        "Rent due? Wrong audience.",
        "The view wasn't listed. It was earned.",
        "Walls this quiet cost seven figures.",
        "Location, location, elevation.",
        "Home is where the equity grows.",
        "They collect likes. He collects keys.",
        "Marble floors, concrete mindset.",
        "The house tour ends where the excuses did.",
        "Square footage is temporary. Skyline is forever.",
        "Buy land. They stopped making it.",
    ],
    "Fashion & Lifestyle": [
        "Dress like the version of you that already made it.",
        "Quiet luxury. Loud results.",
        "The fit is tailored. So is the five-year plan.",
        "Style is saying it once. Class is never repeating it.",
        "Cologne, confidence, and zero notifications.",
        "The suit is armor. The mindset is the weapon.",
        "Look expensive. Think long-term. Move silent.",
        "Some follow trends. Others set standards.",
        "Luxury is not needing anyone to notice.",
        "Every detail intentional. Every room aware.",
        "Overdressed is a myth invented by the underprepared.",
        "The closet is a portfolio. Dress like an investor.",
        "First impressions don't get a second meeting.",
        "Linen in summer, cashmere in winter, standards all year.",
        "He didn't upgrade the wardrobe. He upgraded the man in it.",
    ],
    "Money Mindset": [
        "Broke is a season. Poor is a mindset.",
        "Your network knew before your bank did.",
        "Discipline is the highest form of self-respect.",
        "Rich habits look boring until the results aren't.",
        "The market rewards patience and punishes opinions.",
        "Sacrifice comfort for a decade. Buy freedom for life.",
        "Nobody claps at chapter one. Write it anyway.",
        "Assets buy assets. That's the whole cheat code.",
        "You can't heal in the same environment that broke you — so build a new one.",
        "Silence, savings, and one obsession.",
        "Comfort zones don't pay dividends.",
        "The grind is invisible. The results won't be.",
        "Earn in silence. Let the lifestyle make the announcement.",
        "Motivation fades. Systems compound.",
        "Being underestimated is a tax advantage.",
        "Play long-term games with long-term people.",
        "The first million is a mindset problem, not a math problem.",
        "Spend less than you flex. Until the flex is free.",
        "Poverty screams. Wealth schedules.",
        "One day, or day one. The calendar is watching.",
    ],
    "Engagement Hooks (start your reel with these)": [
        "Watch till the end — the last second is the whole point.",
        "Nobody talks about this side of luxury…",
        "If you're seeing this, the algorithm thinks you're going to make it.",
        "Save this before it disappears from your feed.",
        "This is your sign to stop scrolling and start building.",
        "99% will scroll. This is for the 1%.",
        "Tag someone who's building in silence.",
        "You weren't supposed to see this yet.",
        "Repeat after me: it's not expensive, it's earned.",
        "Comment 'KEYS' if this is the goal.",
        "POV: The life you keep saving to your folder.",
        "Don't watch this broke. Watch it motivated.",
        "The feed shows dreams. The bio shows the way.",
        "Double tap if this is non-negotiable for you.",
        "Follow for the version of you that shows up in 5 years.",
    ],
}

# The Pro 30-pack: strongest hooks across categories.
PRO_30 = (
    CAPTIONS["Supercars"][:5]
    + CAPTIONS["Luxury Watches"][:5]
    + CAPTIONS["Private Jets & Yachts"][:3]
    + CAPTIONS["Real Estate & Interiors"][:3]
    + CAPTIONS["Fashion & Lifestyle"][:4]
    + CAPTIONS["Money Mindset"][:5]
    + CAPTIONS["Engagement Hooks (start your reel with these)"][:5]
)


def wrap(c, text, font, size, max_w):
    """Simple word wrapper returning a list of lines."""
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


def build(filename, title, sub, grouped):
    """grouped: list of (category, [captions])"""
    out = os.path.join(OUT_DIR, filename)
    c = canvas.Canvas(out, pagesize=A4)
    total = sum(len(caps) for _, caps in grouped)

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
        c.drawCentredString(W / 2, 34, f"{STORE}  ·  {title}  ·  Page {page_num}")

    # ── Cover ─────────────────────────────────────────────────
    bg()
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.2)
    c.rect(40, 40, W - 80, H - 80, stroke=1, fill=0)
    c.setLineWidth(0.5)
    c.rect(48, 48, W - 96, H - 96, stroke=1, fill=0)

    c.setFillColor(GOLD_BRIGHT)
    c.setFont("Helvetica", 11)
    c.drawCentredString(W / 2, H - 200, "*   B O N U S   C O N T E N T   *")

    c.setFillColor(TEXT)
    c.setFont("Times-Bold", 40)
    c.drawCentredString(W / 2, H - 295, title)

    c.setFillColor(GOLD_BRIGHT)
    c.setFont("Times-Italic", 16)
    c.drawCentredString(W / 2, H - 330, sub)

    gold_rule(H - 375, W / 2 - 90, W / 2 + 90)

    c.setFillColor(CARD)
    c.roundRect(100, 180, W - 200, 150, 10, stroke=0, fill=1)
    c.setStrokeColor(GOLD)
    c.roundRect(100, 180, W - 200, 150, 10, stroke=1, fill=0)
    c.setFillColor(GOLD_BRIGHT)
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(W / 2, 300, "HOW TO USE THESE HOOKS")
    c.setFillColor(TEXT)
    c.setFont("Helvetica", 10)
    for i, line in enumerate([
        "1.  Use them as the first line of your caption, or as on-screen text",
        "     in the first 2 seconds of the reel — that's what stops the scroll.",
        "2.  Match the hook's niche to the reel you're posting.",
        "3.  End captions with a CTA from the Engagement Hooks section.",
    ]):
        c.drawString(126, 274 - i * 20, line)

    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8)
    c.drawCentredString(W / 2, 120, f"© 2026 {STORE} · For the buyer's use only · Please do not reshare this document")
    c.showPage()

    # ── Caption pages ─────────────────────────────────────────
    page = 2
    n = 0
    y = H - 120

    def new_page():
        nonlocal y
        bg()
        c.setFillColor(GOLD_BRIGHT)
        c.setFont("Times-Bold", 20)
        c.drawString(60, H - 70, title)
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 9)
        c.drawRightString(W - 60, H - 68, f"{total} hooks")
        gold_rule(H - 84)
        y = H - 120

    new_page()
    for cat, caps in grouped:
        if y < 130:
            footer(page)
            c.showPage()
            page += 1
            new_page()
        c.setFillColor(GOLD)
        c.setFont("Helvetica-Bold", 13)
        c.drawString(60, y, cat.upper())
        y -= 26

        for cap in caps:
            n += 1
            lines = wrap(c, cap, "Helvetica", 10, W - 190)
            row_h = 14 + len(lines) * 13
            if y - row_h < 60:
                footer(page)
                c.showPage()
                page += 1
                new_page()
            if n % 2 == 1:
                c.setFillColor(CARD)
                c.rect(55, y - row_h + 16, W - 110, row_h - 4, stroke=0, fill=1)
            c.setFillColor(GOLD_BRIGHT)
            c.setFont("Helvetica-Bold", 9)
            c.drawString(64, y, f"{n:03d}")
            c.setFillColor(TEXT)
            c.setFont("Helvetica", 10)
            for li, line in enumerate(lines):
                c.drawString(95, y - li * 13, line)
            y -= row_h

        y -= 10  # gap after category

    footer(page)
    c.showPage()

    # ── Support page ──────────────────────────────────────────
    bg()
    c.setFillColor(GOLD_BRIGHT)
    c.setFont("Times-Bold", 24)
    c.drawCentredString(W / 2, H - 120, "Make Them Yours")
    gold_rule(H - 140, W / 2 - 120, W / 2 + 120)
    c.setFillColor(TEXT)
    c.setFont("Helvetica", 10)
    c.drawCentredString(W / 2, H - 175, "Swap a word, add your story, test two hooks on the same reel —")
    c.drawCentredString(W / 2, H - 192, "the best caption is the one your audience answers.")

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
    footer(page + 1)
    c.showPage()

    c.save()
    print(f"Created: {filename}  ({page + 1} pages, {total} hooks)")


# Pro 30-pack: one flat group (already a curated mix).
build(
    "Bonus-30-Viral-Hook-Captions.pdf",
    "30 Viral Hook Captions",
    "Creator Pro Vault · Bonus Pack",
    [("Your 30 Scroll-Stoppers", PRO_30)],
)

# Empire 100-pack: full library grouped by niche.
build(
    "Bonus-100-Viral-Hook-Captions.pdf",
    "100 Viral Hook Captions",
    "Empire Vault · Bonus Pack",
    list(CAPTIONS.items()),
)
