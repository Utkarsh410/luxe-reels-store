import LegalLayout from "../components/LegalLayout";

export default function Privacy() {
  return (
    <LegalLayout title="Privacy Policy">
      <p>
        This policy explains what information we handle when you use Luxe Reels Vault and
        make a purchase.
      </p>

      <h2>1. What we collect</h2>
      <p>
        We collect the minimum needed to deliver your order: your payment confirmation
        details from Razorpay (order ID, payment ID, and the bundle you bought). If you
        contact us for support, we also receive whatever contact details you share (email or
        Instagram handle).
      </p>

      <h2>2. What we never see</h2>
      <p>
        Your card number, UPI PIN, and banking credentials are handled entirely by Razorpay
        on their secure checkout. They never touch our servers.
      </p>

      <h2>3. How we use your information</h2>
      <p>
        Solely to verify your payment, deliver your bundle, provide support, and comply with
        tax/accounting obligations. We do not sell or share your data with third parties for
        marketing.
      </p>

      <h2>4. Third-party services</h2>
      <p>
        We rely on: <strong>Razorpay</strong> (payment processing),{" "}
        <strong>Google Drive</strong> (content delivery), and <strong>Vercel</strong>{" "}
        (website hosting). Each processes data under its own privacy policy.
      </p>

      <h2>5. Cookies</h2>
      <p>
        We do not use advertising or tracking cookies. Razorpay&apos;s checkout may set cookies
        required for secure payment processing.
      </p>

      <h2>6. Data retention and your rights</h2>
      <p>
        Payment records are retained as required by Indian law. You can ask us what data we
        hold about you or request deletion of support correspondence by contacting us.
      </p>

      <h2>7. Contact</h2>
      <p>
        Privacy questions: <a href="mailto:utkarsh410@gmail.com">utkarsh410@gmail.com</a> or
        DM{" "}
        <a
          href="https://www.instagram.com/the.millionaire.frame"
          target="_blank"
          rel="noopener noreferrer"
        >
          @the.millionaire.frame
        </a>
        .
      </p>
    </LegalLayout>
  );
}
