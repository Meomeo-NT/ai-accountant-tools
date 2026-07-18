import Link from "next/link";
import type { Metadata } from "next";
import { getMarkdownDoc } from "@/lib/markdown";
import EmailCaptureForm from "@/components/EmailCaptureForm";

export const metadata: Metadata = {
  title: "Templates & Prompts — AI Accountant Tools",
  description:
    "Free AI prompts and Excel templates for accountants. Accounting AI Starter Pack available.",
  keywords: ["accounting templates", "ChatGPT prompts for accountants"],
};

export default async function TemplatesPage() {
  const doc = await getMarkdownDoc("templates", "accountant-ai-prompts");
  return (
    <div>
      <h1 className="text-3xl font-bold text-brand">Templates & Prompts</h1>
      <p className="mt-2 text-sm text-slate-500">
        10 ChatGPT prompts cho kế toán — điền email để nhận file PDF đầy đủ.
      </p>
      <EmailCaptureForm />
      <article
        className="mt-6 prose max-w-none bg-white border rounded-lg p-5"
        dangerouslySetInnerHTML={{ __html: doc.contentHtml }}
      />
      <p className="mt-6 text-sm">
        <Link href="/" className="text-brand">
          ← Back home
        </Link>
      </p>
    </div>
  );
}
