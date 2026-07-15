import { PRODUCTS } from "../../../lib/products";
import { responseHash, safeEqualHex } from "../../../lib/payu";
import { signAccessToken } from "../../../lib/sign";

// PayU redirects the buyer's browser here (POST) after payment,
// for both success and failure (surl === furl).
export default function handler(req, res) {
  if (req.method !== "POST") {
    // A stray GET (e.g. someone opening the URL directly) → home.
    return res.redirect(302, "/");
  }

  const b = req.body || {};
  const salt = process.env.PAYU_MERCHANT_SALT;
  const key = process.env.PAYU_MERCHANT_KEY;

  const expected = responseHash({
    salt,
    status: b.status,
    udf1: b.udf1 || "",
    udf2: b.udf2 || "",
    udf3: b.udf3 || "",
    udf4: b.udf4 || "",
    udf5: b.udf5 || "",
    email: b.email || "",
    firstname: b.firstname || "",
    productinfo: b.productinfo || "",
    amount: b.amount || "",
    txnid: b.txnid || "",
    key,
    additionalCharges: b.additionalCharges,
  });

  const genuine = safeEqualHex(expected, b.hash || "");
  const bundleId = b.udf1;
  const product = PRODUCTS[bundleId];

  // Reject anything that isn't a genuine, successful payment for a real
  // bundle at the correct price.
  const priceOk = product && Number(b.amount) === product.price / 100;
  if (!genuine || b.status !== "success" || !product || !priceOk) {
    return res.redirect(302, "/?payment=failed");
  }

  const token = signAccessToken({
    bundleId,
    paymentId: b.mihpayid || b.txnid,
    orderId: b.txnid,
    ts: Date.now(),
  });

  return res.redirect(303, `/success?token=${encodeURIComponent(token)}`);
}
