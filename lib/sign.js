import crypto from "crypto";

const secret = () => process.env.RAZORPAY_KEY_SECRET || "dev-secret";

// Sign a payload so the success page can only be opened after a real,
// server-verified payment. Token = base64(payload).hmac
export function signAccessToken(payload) {
  const data = Buffer.from(JSON.stringify(payload)).toString("base64url");
  const sig = crypto.createHmac("sha256", secret()).update(data).digest("hex");
  return `${data}.${sig}`;
}

export function verifyAccessToken(token) {
  if (!token || typeof token !== "string" || !token.includes(".")) return null;
  const [data, sig] = token.split(".");
  const expected = crypto.createHmac("sha256", secret()).update(data).digest("hex");
  const a = Buffer.from(sig, "utf8");
  const b = Buffer.from(expected, "utf8");
  if (a.length !== b.length || !crypto.timingSafeEqual(a, b)) return null;
  try {
    return JSON.parse(Buffer.from(data, "base64url").toString("utf8"));
  } catch {
    return null;
  }
}
