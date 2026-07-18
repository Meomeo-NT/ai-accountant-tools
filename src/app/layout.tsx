import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";

export const metadata: Metadata = {
  title: "AI Accountant Tools — Smart Accounting Toolkit",
  description:
    "AI helps accountants work faster without replacing accounting judgement. Tools, templates and workflows for accounting automation.",
  keywords: [
    "AI tools for accountants",
    "accounting automation",
    "AI workflow for finance",
    "Excel automation for accounting",
  ],
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="min-h-screen flex flex-col">
        <header className="bg-brand text-white">
          <nav className="max-w-5xl mx-auto px-4 py-4 flex flex-wrap gap-4 text-sm">
            <Link href="/" className="font-bold mr-4">
              AI Accountant Tools
            </Link>
            <Link href="/workflows">Workflows</Link>
            <Link href="/tools">Tools</Link>
            <Link href="/templates">Templates</Link>
            <Link href="/comparisons">Comparisons</Link>
          </nav>
        </header>
        <main className="flex-1 max-w-5xl mx-auto px-4 py-8 w-full">
          {children}
        </main>
        <footer className="bg-slate-800 text-slate-300 text-xs text-center py-6 px-4">
          <p>
            AI Accountant Tools does not replace accounting judgement or
            regulatory compliance. AI recommendations should always be reviewed
            by qualified accounting professionals.
          </p>
          <p className="mt-2">
            We may earn commissions from some links on this site, at no extra
            cost to you. This does not affect the objectivity of our content.
          </p>
        </footer>
      </body>
    </html>
  );
}
