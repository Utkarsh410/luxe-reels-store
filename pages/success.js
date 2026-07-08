import { verifyAccessToken } from "../lib/sign";
import { PRODUCTS, getDriveLink } from "../lib/products";

export async function getServerSideProps({ query }) {
  const payload = verifyAccessToken(query.token);
  if (!payload || !PRODUCTS[payload.bundleId]) {
    return { redirect: { destination: "/", permanent: false } };
  }
  const product = PRODUCTS[payload.bundleId];
  return {
    props: {
      bundleName: product.name,
      reels: product.reels,
      paymentId: payload.paymentId,
      driveLink: getDriveLink(payload.bundleId) || "",
    },
  };
}

export default function Success({ bundleName, reels, paymentId, driveLink }) {
  return (
    <main className="success-page">
      <div className="success-card">
        <div className="check">✓</div>
        <h1>Payment Successful</h1>
        <p className="sub">
          Welcome to the <strong>{bundleName}</strong> — {reels} are now yours.
        </p>

        {driveLink ? (
          <a href={driveLink} target="_blank" rel="noopener noreferrer" className="btn btn-gold big">
            📂 Open Your Vault on Google Drive
          </a>
        ) : (
          <p className="error">
            Your payment is confirmed, but the delivery link isn&apos;t configured yet. DM us
            on Instagram at{" "}
            <a
              href="https://www.instagram.com/the.millionaire.frame"
              target="_blank"
              rel="noopener noreferrer"
            >
              @the.millionaire.frame
            </a>{" "}
            with your payment ID and we&apos;ll send it right away.
          </p>
        )}

        <div className="receipt">
          <p>
            Payment ID: <code>{paymentId}</code>
          </p>
          <p className="fine">
            Save this page or screenshot your payment ID. Inside the Drive folder you&apos;ll
            find a PDF with download links for every reel in your bundle. Need help? DM{" "}
            <a
              href="https://www.instagram.com/the.millionaire.frame"
              target="_blank"
              rel="noopener noreferrer"
            >
              @the.millionaire.frame
            </a>
            .
          </p>
        </div>

        <a href="/" className="back">
          ← Back to store
        </a>
      </div>
    </main>
  );
}
