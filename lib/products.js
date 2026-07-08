// ─────────────────────────────────────────────────────────────
// EDIT THIS FILE to change your bundles, prices and Drive links.
// Prices are in INR paise (₹499 = 49900).
// The driveLink for each bundle comes from environment variables
// so your links are never exposed in client-side code.
// ─────────────────────────────────────────────────────────────

export const PRODUCTS = {
  starter: {
    id: "starter",
    name: "Starter Vault",
    tagline: "Your entry into luxury content",
    reels: "50 Luxury Reels",
    price: 49900,
    displayPrice: "₹499",
    originalPrice: "₹999",
    features: [
      "50 premium luxury-themed reels",
      "Full HD, watermark-free",
      "Cars, watches, lifestyle niches",
      "Instant PDF access after payment",
      "Repost-ready with trending audio ideas",
    ],
    featured: false,
  },
  pro: {
    id: "pro",
    name: "Creator Pro Vault",
    tagline: "The bestseller for serious pages",
    reels: "150 Luxury Reels",
    price: 99900,
    displayPrice: "₹999",
    originalPrice: "₹2,499",
    features: [
      "150 premium luxury-themed reels",
      "4K + Full HD, watermark-free",
      "Cars, watches, jets, real estate, lifestyle",
      "Bonus: 30 viral hook captions",
      "Instant PDF access after payment",
      "Free updates for 3 months",
    ],
    featured: true,
  },
  empire: {
    id: "empire",
    name: "Empire Vault",
    tagline: "Everything. For pages built to scale",
    reels: "300+ Luxury Reels",
    price: 199900,
    displayPrice: "₹1,999",
    originalPrice: "₹4,999",
    features: [
      "300+ premium luxury-themed reels",
      "4K + Full HD, watermark-free",
      "Every niche: cars, watches, jets, yachts, fashion",
      "Bonus: 100 viral hook captions",
      "Bonus: Monetization playbook PDF",
      "Lifetime free updates",
    ],
    featured: false,
  },
};

// Server-only: maps bundle → Google Drive link (set these in .env.local)
export function getDriveLink(bundleId) {
  const links = {
    starter: process.env.DRIVE_LINK_STARTER,
    pro: process.env.DRIVE_LINK_PRO,
    empire: process.env.DRIVE_LINK_EMPIRE,
  };
  return links[bundleId] || null;
}
