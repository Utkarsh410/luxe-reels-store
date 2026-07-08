import crypto from "crypto";
import { PRODUCTS } from "../../lib/products";
import { signAccessToken } from "../../lib/sign";

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  const {
    razorpay_order_id,
    razorpay_payment_id,
    razorpay_signature,
    bundleId,
  } = req.body || {};

  if (!razorpay_order_id || !razorpay_payment_id || !razorpay_signature || !PRODUCTS[bundleId]) {
    return res.status(400).json({ error: "Missing payment details" });
  }

  // Razorpay's documented verification: HMAC-SHA256(order_id|payment_id, key_secret)
  const expected = crypto
    .createHmac("sha256", process.env.RAZORPAY_KEY_SECRET)
    .update(`${razorpay_order_id}|${razorpay_payment_id}`)
    .digest("hex");

  const valid =
    expected.length === razorpay_signature.length &&
    crypto.timingSafeEqual(Buffer.from(expected), Buffer.from(razorpay_signature));

  if (!valid) {
    return res.status(400).json({ error: "Payment verification failed" });
  }

  // Payment is genuine — issue a signed access token for the success page.
  const token = signAccessToken({
    bundleId,
    paymentId: razorpay_payment_id,
    orderId: razorpay_order_id,
    ts: Date.now(),
  });

  return res.status(200).json({ redirect: `/success?token=${encodeURIComponent(token)}` });
}
