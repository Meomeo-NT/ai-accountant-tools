import type { Metadata } from "next";
import Link from "next/link";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

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
      <body className={`${inter.className} min-h-screen flex flex-col`}>
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
        <main className="flex-1 max-w-6xl mx-auto px-4 py-16 w-full">
          {children}
        </main>
        <footer className="bg-slate-800 text-slate-300 text-xs text-center py-6 px-4">
          <p>
            AI Accountant Tools does not replace accounting judgement or
            regulatory compliance. AI recommendations should always be reviewed
            by qualified accounting professionals.
          </p>
          <p className="mt-2 text-slate-400">
            Minh bạch: Kế Toán AI là một chuyên mục độc lập. Chúng tôi có thể
            nhận hoa hồng liên kết (affiliate) từ một số công cụ được giới thiệu
            trong bài viết nếu bạn đăng ký sử dụng. Điều này không làm tăng chi phí
            của bạn và hoàn toàn không ảnh hưởng đến tính khách quan, trung thực
            của các bài đánh giá.
          </p>
        </footer>
      </body>
    </html>
  );
}
