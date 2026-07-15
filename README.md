# Luxe Reels Vault 💎

A luxury-themed storefront for selling Instagram reels bundles with PayU
payments and instant Google Drive delivery.

## How it works

1. Buyer picks a bundle, enters name/email/phone, and is redirected to PayU's
   secure checkout (UPI / cards / net banking / wallets).
2. PayU sends the result back to `/api/payu/callback`, which verifies the
   SHA-512 response hash and re-checks the amount — no fake access possible.
3. On a genuine success the buyer is redirected to a signed success page
   showing the Google Drive link for that bundle. The Drive folder holds a
   PDF listing every reel link.

## Setup (one time)

1. **PayU keys** — sign up at [payu.in](https://www.payu.in), complete
   onboarding, then Dashboard → Settings → copy your **Merchant Key** and
   **Merchant Salt** into `.env.local`. Keep `PAYU_MODE=test` while testing;
   set it to `live` to accept real money.
2. **APP_SECRET** — set any long random string in `.env.local`; it signs the
   post-payment access token.
3. **Drive links** — upload each bundle PDF to Google Drive, set sharing to
   *Anyone with the link → Viewer*, and paste the links into `.env.local`.
4. **Prices & bundles** — edit `lib/products.js`.

> The repo ships with PayU's public sandbox test key/salt (`gtKFFx` /
> `eCwWELxi`) so you can try the flow immediately. Replace them with your own
> before going live.

## Run locally

```bash
npm install
npm run dev
```

Open http://localhost:3000 and buy a bundle. On PayU's test page use their
sandbox test card (e.g. card 5123456789012346, any future expiry, CVV 123,
OTP 123456) to simulate a full purchase.

## Deploy (free)

Push to GitHub, import at [vercel.com](https://vercel.com), and add the
environment variables from `.env.local` in the Vercel project settings.
Put the deployed URL in your Instagram bio link.

## Files that matter

- `lib/products.js` — bundle names, prices, features
- `lib/payu.js` — PayU hash generation + verification
- `pages/index.js` — landing page + checkout modal
- `pages/success.js` — post-payment delivery page
- `pages/api/payu/create.js` — builds the signed PayU payment request
- `pages/api/payu/callback.js` — verifies PayU's response, unlocks access
