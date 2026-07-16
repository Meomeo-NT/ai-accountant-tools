import Link from "next/link";
import type { Metadata } from "next";
import { getAllWorkflows } from "@/lib/workflows";

export const metadata: Metadata = {
  title: "Accounting Workflows — AI Accountant Tools",
  description:
    "Real accounting workflows showing how AI assists without replacing accounting judgement. Invoice, reconciliation, month-end closing.",
  keywords: [
    "accounting workflows",
    "AI for invoice processing",
    "AI bank reconciliation",
    "month end closing automation",
  ],
};

export default function WorkflowsPage() {
  const workflows = getAllWorkflows();
  return (
    <div>
      <h1 className="text-3xl font-bold text-brand">Accounting Workflows</h1>
      <p className="mt-2 text-slate-600">
        AI assists accountants at the task level — never replacing professional
        judgement or controls.
      </p>
      <div className="mt-6 grid md:grid-cols-2 gap-4">
        {workflows.map((w) => (
          <Link
            key={w.slug}
            href={`/workflows/${w.slug}`}
            className="block border rounded-lg p-5 bg-white hover:shadow"
          >
            <h2 className="text-xl font-bold">{w.name}</h2>
            <p className="text-sm text-slate-600 mt-2">{w.problem}</p>
            <div className="mt-3 flex flex-wrap gap-2 text-xs">
              <span className="bg-slate-100 px-2 py-1 rounded">
                {w.difficulty}
              </span>
              <span className="bg-slate-100 px-2 py-1 rounded">
                saves {w.time_saved}
              </span>
              <span className="bg-slate-100 px-2 py-1 rounded">
                {w.tools.length} tools
              </span>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}