import { useState } from "react";
import { useRouter } from "next/router";
import { PRODUCTS } from "../lib/products";
import SiteFooter from "../components/SiteFooter";

const FAQS = [
  {
    q: "How do I get the reels after paying?",
    a: "Instantly. As soon as your payment is confirmed you're taken to a private access page with your Google Drive link. The Drive folder contains a PDF with download links for every reel in your bundle.",
  },
  {
    q: "Can I repost these on my Instagram page?",
    a: "Yes — that's exactly what they're for. All reels are watermark-free and ready to post on your luxury, motivation or lifestyle theme page.",
  },
  {
    q: "What niches are covered?",
    a: "Supercars, luxury watches, private jets, yachts, real estate, fashion and high-end lifestyle. The bigger bundles cover every niche.",
  },
  {
    q: "What payment methods are supported?",
    a: "UPI, all major credit/debit cards, net banking and wallets — securely processed by PayU.",
  },
  {
    q: "Is this a one-time payment?",
    a: "Yes. Pay once, keep the bundle forever. Pro and Empire vaults also include free content updates.",
  },
];

export default function Home() {
  const router = useRouter();
  const [selected, setSelected] = useState(null); // bundle object being purchased
  const [form, setForm] = useState({ name: "", email: "", phone: "" });
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");
  const [openFaq, setOpenFaq] = useState(0);

  const paymentFailed = router.query.payment === "failed";

  function openCheckout(bundle) {
    setError("");
    setSelected(bundle);
  }

  function closeCheckout() {
    if (submitting) return;
    setSelected(null);
  }

  async function proceedToPay(e) {
    e.preventDefault();
    setError("");

    if (!/^\S+@\S+\.\S+$/.test(form.email)) {
      setError("Please enter a valid email address.");
      return;
    }
    if (!/^\d{10}$/.test(form.phone.replace(/\D/g, "").slice(-10))) {
      setError("Please enter a valid 10-digit phone number.");
      return;
    }

    setSubmitting(true);
    try {
      const res = await fetch("/api/payu/create", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ bundleId: selected.id, ...form }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Something went wrong");

      // Build and submit a hidden form → browser redirects to PayU's checkout.
      const payuForm = document.createElement("form");
      payuForm.method = "POST";
      payuForm.action = data.action;
      Object.entries(data.params).forEach(([k, v]) => {
        const input = document.createElement("input");
        input.type = "hidden";
        input.name = k;
        input.value = v;
        payuForm.appendChild(input);
      });
      document.body.appendChild(payuForm);
      payuForm.submit();
    } catch (err) {
      setError(err.message);
      setSubmitting(false);
    }
  }

  return (
    <main>
      {/* ── Hero ─────────────────────────────── */}
      <section className="hero">
        <div className="hero-glow" aria-hidden="true" />
        <p className="eyebrow">✦ Premium Content Vault ✦</p>
        <h1>
          Luxury Reels That <em>Grow</em> Your Page
        </h1>
        <p className="sub">
          Ready-to-post, watermark-free luxury themed reels — supercars, watches,
          jets &amp; lifestyle. Pay once, get instant access, post daily.
        </p>
        <div className="hero-cta">
          <a href="#pricing" className="btn btn-gold">
            Get Your Vault
          </a>
          <a href="#how" className="btn btn-ghost">
            How it works
          </a>
        </div>
        <div className="stats">
          <div>
            <strong>500+</strong>
            <span>Reels in library</span>
          </div>
          <div>
            <strong>4K</strong>
            <span>Ultra HD quality</span>
          </div>
          <div>
            <strong>Instant</strong>
            <span>Delivery via Drive</span>
          </div>
        </div>
      </section>

      {/* ── How it works ─────────────────────── */}
      <section className="how" id="how">
        <h2>Three Steps to Content Freedom</h2>
        <div className="how-grid">
          <div className="how-card">
            <span className="how-num">01</span>
            <h3>Pick your vault</h3>
            <p>Choose the bundle that fits your page — from starter to full empire.</p>
          </div>
          <div className="how-card">
            <span className="how-num">02</span>
            <h3>Pay securely</h3>
            <p>UPI, cards, net banking — handled end-to-end by PayU.</p>
          </div>
          <div className="how-card">
            <span className="how-num">03</span>
            <h3>Get instant access</h3>
            <p>Your private Google Drive link unlocks a PDF with every reel download link.</p>
          </div>
        </div>
      </section>

      {/* ── Pricing ──────────────────────────── */}
      <section className="pricing" id="pricing">
        <h2>Choose Your Vault</h2>
        <p className="pricing-sub">One-time payment. Lifetime access. No subscriptions.</p>
        {paymentFailed && (
          <p className="error">
            Your payment didn&apos;t go through and you were not charged. Please try again.
          </p>
        )}
        <div className="cards">
          {Object.values(PRODUCTS).map((p) => (
            <div key={p.id} className={`card${p.featured ? " featured" : ""}`}>
              {p.featured && <span className="badge">Most Popular</span>}
              <h3>{p.name}</h3>
              <p className="tagline">{p.tagline}</p>
              <p className="reels">{p.reels}</p>
              <p className="price">
                <s>{p.originalPrice}</s> {p.displayPrice}
              </p>
              <ul>
                {p.features.map((f) => (
                  <li key={f}>{f}</li>
                ))}
              </ul>
              <button
                className={`btn ${p.featured ? "btn-gold" : "btn-outline"}`}
                onClick={() => openCheckout(p)}
              >
                {`Unlock for ${p.displayPrice}`}
              </button>
            </div>
          ))}
        </div>
        <p className="secure">🔒 Secured by PayU · UPI · Cards · Net Banking · Wallets</p>
      </section>

      {/* ── FAQ ──────────────────────────────── */}
      <section className="faq">
        <h2>Questions, Answered</h2>
        {FAQS.map((f, i) => (
          <div key={f.q} className={`faq-item${openFaq === i ? " open" : ""}`}>
            <button className="faq-q" onClick={() => setOpenFaq(openFaq === i ? -1 : i)}>
              {f.q}
              <span>{openFaq === i ? "−" : "+"}</span>
            </button>
            {openFaq === i && <p className="faq-a">{f.a}</p>}
          </div>
        ))}
      </section>

      <SiteFooter />

      {/* ── Checkout modal ───────────────────── */}
      {selected && (
        <div className="modal-overlay" onClick={closeCheckout}>
          <div className="modal" onClick={(e) => e.stopPropagation()}>
            <button className="modal-close" onClick={closeCheckout} aria-label="Close">
              ×
            </button>
            <h3>Checkout</h3>
            <p className="modal-sub">
              {selected.name} · {selected.reels}
            </p>
            <p className="modal-price">{selected.displayPrice}</p>

            <form onSubmit={proceedToPay}>
              <label>
                Full name
                <input
                  type="text"
                  required
                  value={form.name}
                  onChange={(e) => setForm({ ...form, name: e.target.value })}
                  placeholder="Your name"
                />
              </label>
              <label>
                Email
                <input
                  type="email"
                  required
                  value={form.email}
                  onChange={(e) => setForm({ ...form, email: e.target.value })}
                  placeholder="you@example.com"
                />
              </label>
              <label>
                Phone
                <input
                  type="tel"
                  required
                  value={form.phone}
                  onChange={(e) => setForm({ ...form, phone: e.target.value })}
                  placeholder="10-digit mobile number"
                />
              </label>
              {error && <p className="error modal-error">{error}</p>}
              <button type="submit" className="btn btn-gold big" disabled={submitting}>
                {submitting ? "Redirecting to PayU…" : `Pay ${selected.displayPrice} securely`}
              </button>
            </form>
            <p className="modal-fine">
              🔒 You&apos;ll be redirected to PayU&apos;s secure checkout. We never see your card
              or UPI details.
            </p>
          </div>
        </div>
      )}
    </main>
  );
}
