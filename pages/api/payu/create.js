import { PRODUCTS } from "../../../lib/products";
import { payuBase, makeTxnId, requestHash } from "../../../lib/payu";

export default function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  const { bundleId, name, email, phone } = req.body || {};
  const product = PRODUCTS[bundleId];
  if (!product) {
    return res.status(400).json({ error: "Unknown bundle" });
  }
  if (!name || !email || !phone) {
    return res.status(400).json({ error: "Name, email and phone are required" });
  }

  const key = process.env.PAYU_MERCHANT_KEY;
  const salt = process.env.PAYU_MERCHANT_SALT;
  if (!key || !salt) {
    return res.status(500).json({
      error: "PayU keys not configured. Add PAYU_MERCHANT_KEY and PAYU_MERCHANT_SALT to .env.local",
    });
  }

  // Amount always comes from the server-side catalog — never the client.
  const amount = (product.price / 100).toFixed(2);
  const txnid = makeTxnId();
  const productinfo = product.name;
  const firstname = String(name).trim().slice(0, 60);

  const proto = req.headers["x-forwarded-proto"] || "http";
  const base = `${proto}://${req.headers.host}`;

  const params = {
    key,
    txnid,
    amount,
    productinfo,
    firstname,
    email: String(email).trim(),
    phone: String(phone).trim(),
    surl: `${base}/api/payu/callback`,
    furl: `${base}/api/payu/callback`,
    udf1: bundleId, // carried through so the callback knows which bundle to unlock
  };

  params.hash = requestHash({ ...params, salt });

  return res.status(200).json({ action: payuBase(), params });
}
