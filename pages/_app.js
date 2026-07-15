import Head from "next/head";
import "../styles/globals.css";

export default function App({ Component, pageProps }) {
  return (
    <>
      <Head>
        <title>Luxe Reels Vault — Premium Luxury Reels Bundles</title>
        <meta
          name="description"
          content="Ready-to-post luxury themed Instagram reels bundles. Instant access after payment."
        />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>
      <Component {...pageProps} />
    </>
  );
}
