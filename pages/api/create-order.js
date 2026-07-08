import Razorpay from "razorpay";
import { PRODUCTS } from "../../lib/products";

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  const { bundleId } = req.body || {};
  const product = PRODUCTS[bundleId];
  if (!product) {
    return res.status(400).json({ error: "Unknown bundle" });
  }

  if (!process.env.RAZORPAY_KEY_ID || !process.env.RAZORPAY_KEY_SECRET) {
    return res.status(500).json({
      error:
        "Razorpay keys not configured. Add RAZORPAY_KEY_ID and RAZORPAY_KEY_SECRET to .env.local",
    });
  }

  try {
    const razorpay = new Razorpay({
      key_id: process.env.RAZORPAY_KEY_ID,
      key_secret: process.env.RAZORPAY_KEY_SECRET,
    });

    // Amount always comes from the server-side catalog — never from the client.
    const order = await razorpay.orders.create({
      amount: product.price,
      currency: "INR",
      receipt: `${bundleId}_${Date.now()}`,
      notes: { bundleId, bundleName: product.name },
    });

    return res.status(200).json({
      orderId: order.id,
      amount: order.amount,
      currency: order.currency,
      keyId: process.env.RAZORPAY_KEY_ID,
      bundleName: product.name,
    });
  } catch (err) {
    console.error("create-order failed:", err);
    return res.status(500).json({ error: "Could not create order. Try again." });
  }
}
