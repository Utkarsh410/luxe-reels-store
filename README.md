# Luxe Reels Vault 💎

A luxury-themed storefront for selling Instagram reels bundles with Razorpay
payments and instant Google Drive delivery.

## How it works

1. Buyer picks a bundle and pays via Razorpay (UPI / cards / net banking).
2. The server verifies the payment signature (HMAC-SHA256) — no fake access possible.
3. Buyer is redirected to a signed success page showing the Google Drive link
   for that bundle. The Drive folder holds a PDF listing every reel link.

## Setup (one time)

1. **Razorpay keys** — sign up at [razorpay.com](https://razorpay.com), complete KYC,
   then Dashboard → Settings → API Keys → Generate. Put both keys in `.env.local`.
   Use `rzp_test_...` keys to test, `rzp_live_...` to accept real money.
2. **Drive links** — upload each bundle PDF to Google Drive, set sharing to
   *Anyone with the link → Viewer*, and paste the links into `.env.local`.
3. **Prices & bundles** — edit `lib/products.js`.

## Run locally

```bash
npm install
npm run dev
```

Open http://localhost:3000. With `rzp_test_` keys, use Razorpay's test
cards/UPI (success@razorpay) to simulate a full purchase.

## Deploy (free)

Push to GitHub, import at [vercel.com](https://vercel.com), and add the five
environment variables from `.env.local` in the Vercel project settings.
Put the deployed URL in your Instagram bio link.

## Files that matter

- `lib/products.js` — bundle names, prices, features
- `pages/index.js` — landing page
- `pages/success.js` — post-payment delivery page
- `pages/api/create-order.js` — creates the Razorpay order (server-side price)
- `pages/api/verify-payment.js` — verifies the payment signature
