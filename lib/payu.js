import crypto from "crypto";

// ─────────────────────────────────────────────────────────────
// PayU India integration helpers.
//
// PayU uses a redirect flow: we POST a signed form to PayU's
// hosted checkout, the buyer pays there, then PayU POSTs the
// result back to our callback URL. Every request/response is
// signed with a SHA-512 hash using your Merchant Salt.
//
// This uses PayU's current 10-UDF hash format. If PayU support
// ever tells you to use the legacy 5-UDF format, remove the five
// empty udf6–udf10 slots from the arrays below.
// ─────────────────────────────────────────────────────────────

export function payuBase() {
  return (process.env.PAYU_MODE || "test") === "live"
    ? "https://secure.payu.in/_payment"
    : "https://test.payu.in/_payment";
}

export function makeTxnId() {
  return `LRV${Date.now()}${crypto.randomBytes(3).toString("hex")}`;
}

// Forward hash sent with the payment request.
export function requestHash({ key, txnid, amount, productinfo, firstname, email, udf1 = "", udf2 = "", udf3 = "", udf4 = "", udf5 = "", salt }) {
  const parts = [
    key, txnid, amount, productinfo, firstname, email,
    udf1, udf2, udf3, udf4, udf5,
    "", "", "", "", "", // udf6–udf10 (unused)
    salt,
  ];
  return crypto.createHash("sha512").update(parts.join("|")).digest("hex");
}

// Reverse hash PayU sends back — used to verify the response is genuine.
export function responseHash({ salt, status, udf1 = "", udf2 = "", udf3 = "", udf4 = "", udf5 = "", email, firstname, productinfo, amount, txnid, key, additionalCharges }) {
  const parts = [
    salt, status,
    "", "", "", "", "", // udf10–udf6 (unused)
    udf5, udf4, udf3, udf2, udf1,
    email, firstname, productinfo, amount, txnid, key,
  ];
  const base = parts.join("|");
  // If PayU adds a convenience fee, it is prepended to the hash string.
  const str = additionalCharges ? `${additionalCharges}|${base}` : base;
  return crypto.createHash("sha512").update(str).digest("hex");
}

export function safeEqualHex(a, b) {
  if (!a || !b || a.length !== b.length) return false;
  return crypto.timingSafeEqual(Buffer.from(a, "hex"), Buffer.from(b, "hex"));
}
