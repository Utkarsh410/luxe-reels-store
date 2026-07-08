export default function SiteFooter() {
  return (
    <footer>
      <p>💎 Luxe Reels Vault</p>
      <p className="fine">
        Instant digital delivery · One-time payment ·{" "}
        <a
          href="https://www.instagram.com/the.millionaire.frame"
          target="_blank"
          rel="noopener noreferrer"
        >
          @the.millionaire.frame
        </a>
      </p>
      <nav className="footer-links">
        <a href="/contact">Contact Us</a>
        <a href="/terms">Terms &amp; Conditions</a>
        <a href="/privacy">Privacy Policy</a>
        <a href="/refunds">Refund Policy</a>
      </nav>
    </footer>
  );
}
