import { useState } from "react";
import { useRouter } from "next/router";
import { PRODUCTS } from "../lib/products";

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
    a: "UPI, all major credit/debit cards, net banking and wallets — securely processed by Razorpay.",
  },
  {
    q: "Is this a one-time payment?",
    a: "Yes. Pay once, keep the bundle forever. Pro and Empire vaults also include free content updates.",
  },
];

export default function Home() {
  const router = useRouter();
  const [loadingId, setLoadingId] = useState(null);
  const [error, setError] = useState("");
  const [openFaq, setOpenFaq] = useState(0);

  async function buy(bundleId) {
    setError("");
    setLoadingId(bundleId);
    try {
      const res = await fetch("/api/create-order", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ bundleId }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Something went wrong");

      if (typeof window.Razorpay === "undefined") {
        throw new Error("Payment gateway is still loading — try again in a moment.");
      }

      const rzp = new window.Razorpay({
        key: data.keyId,
        amount: data.amount,
        currency: data.currency,
        order_id: data.orderId,
        name: "Luxe Reels Vault",
        description: data.bundleName,
        theme: { color: "#c9a227" },
        handler: async (response) => {
          try {
            const verifyRes = await fetch("/api/verify-payment", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ ...response, bundleId }),
            });
            const verifyData = await verifyRes.json();
            if (!verifyRes.ok) throw new Error(verifyData.error || "Verification failed");
            router.push(verifyData.redirect);
          } catch (e) {
            setError(e.message);
          }
        },
        modal: { ondismiss: () => setLoadingId(null) },
      });
      rzp.on("payment.failed", () => {
        setError("Payment failed. No money was deducted permanently — please try again.");
        setLoadingId(null);
      });
      rzp.open();
    } catch (e) {
      setError(e.message);
      setLoadingId(null);
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
            <p>UPI, cards, net banking — handled end-to-end by Razorpay.</p>
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
        {error && <p className="error">{error}</p>}
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
                onClick={() => buy(p.id)}
                disabled={loadingId !== null}
              >
                {loadingId === p.id ? "Opening secure checkout…" : `Unlock for ${p.displayPrice}`}
              </button>
            </div>
          ))}
        </div>
        <p className="secure">🔒 Secured by Razorpay · UPI · Cards · Net Banking · Wallets</p>
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

      <footer>
        <p>💎 Luxe Reels Vault</p>
        <p className="fine">
          Instant digital delivery · One-time payment · Support: DM us on Instagram
        </p>
      </footer>
    </main>
  );
}
