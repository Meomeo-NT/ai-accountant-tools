import Link from "next/link";
import type { Metadata } from "next";
import { getAllTools } from "@/lib/tools";

export const metadata: Metadata = {
  title: "AI Tools for Accountants — AI Accountant Tools",
  description:
    "Curated AI tools for accounting tasks: invoice OCR, Excel automation, reporting, analysis. Reviewed for accountants and finance teams.",
  keywords: ["AI tools for accountants", "accounting software AI", "Excel AI"],
};

export default function ToolsPage() {
  const tools = getAllTools();
  return (
    <div>
      <h1 className="text-3xl font-bold text-brand">AI Tools for Accountants</h1>
      <div className="mt-6 grid md:grid-cols-2 gap-4">
        {tools.map((t) => (
          <Link
            key={t.slug}
            href={`/tools/${t.slug}`}
            className="block border rounded-lg p-5 bg-white hover:shadow"
          >
            <div className="flex justify-between items-start">
              <h2 className="text-xl font-bold">{t.name}</h2>
              <span className="text-xs bg-slate-100 px-2 py-1 rounded">
                {t.category}
              </span>
            </div>
            <p className="text-sm text-slate-600 mt-2">{t.description}</p>
            <div className="mt-3 flex flex-wrap gap-1 text-xs text-slate-500">
              {t.target_user.map((u) => (
                <span key={u} className="bg-slate-50 px-2 py-1 rounded">
                  {u}
                </span>
              ))}
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}