import Script from "next/script";
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
      <Script src="https://checkout.razorpay.com/v1/checkout.js" strategy="lazyOnload" />
      <Component {...pageProps} />
    </>
  );
}
