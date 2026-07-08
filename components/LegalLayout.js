import Head from "next/head";
import SiteFooter from "./SiteFooter";

export default function LegalLayout({ title, children }) {
  return (
    <>
      <Head>
        <title>{`${title} — Luxe Reels Vault`}</title>
      </Head>
      <main className="legal">
        <a href="/" className="back">
          ← Back to store
        </a>
        <h1>{title}</h1>
        <p className="updated">Last updated: 8 July 2026</p>
        {children}
        <SiteFooter />
      </main>
    </>
  );
}
