import LegalLayout from "../components/LegalLayout";

export default function Contact() {
  return (
    <LegalLayout title="Contact Us">
      <p>
        We&apos;re a small creator-run business and we respond fast. Reach us through any of
        these channels:
      </p>
      <h2>Instagram (fastest)</h2>
      <p>
        DM us at{" "}
        <a
          href="https://www.instagram.com/the.millionaire.frame"
          target="_blank"
          rel="noopener noreferrer"
        >
          @the.millionaire.frame
        </a>{" "}
        — we typically reply within a few hours.
      </p>
      <h2>Email</h2>
      <p>
        <a href="mailto:utkarsh410@gmail.com">utkarsh410@gmail.com</a> — for payment issues,
        include your Razorpay Payment ID (shown on your success page) so we can resolve it
        quickly.
      </p>
      <h2>Support hours</h2>
      <p>
        Monday to Saturday, 10:00 AM – 8:00 PM IST. Payment and access issues are resolved
        within 24 hours.
      </p>
    </LegalLayout>
  );
}
