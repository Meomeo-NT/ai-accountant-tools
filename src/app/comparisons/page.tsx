import type { Metadata } from "next";
import { getMarkdownDoc } from "@/lib/markdown";

export const metadata: Metadata = {
  title: "AI Comparisons for Accountants — AI Accountant Tools",
  description:
    "ChatGPT vs Claude for accountants, Excel Copilot vs ChatGPT, and more practical comparisons.",
  keywords: ["ChatGPT vs Claude accountants", "Excel Copilot vs ChatGPT"],
};

export default async function ComparisonsPage() {
  const doc = await getMarkdownDoc("comparisons", "chatgpt-vs-claude");
  return (
    <div>
      <h1 className="text-3xl font-bold text-brand">Comparisons</h1>
      <article
        className="mt-4 prose max-w-none bg-white border rounded-lg p-5"
        dangerouslySetInnerHTML={{ __html: doc.contentHtml }}
      />
    </div>
  );
}