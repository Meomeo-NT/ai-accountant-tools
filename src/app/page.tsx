import Link from "next/link";
import { getAllWorkflows } from "@/lib/workflows";
import { getAllTools } from "@/lib/tools";

export default function HomePage() {
  const workflows = getAllWorkflows();
  const tools = getAllTools().slice(0, 6);

  return (
    <div>
      <section className="text-center py-10">
        <h1 className="text-4xl font-bold text-brand">
          AI Accountant Tools
        </h1>
        <p className="mt-4 text-lg text-slate-600">
          Smart Accounting Toolkit — tools, templates and AI workflows that help
          accountants work faster.
        </p>
        <p className="mt-2 text-sm text-slate-500 italic">
          AI helps accountants work faster without replacing accounting
          judgement.
        </p>
        <div className="mt-6 flex justify-center gap-3">
          <Link
            href="/workflows"
            className="bg-brand text-white px-5 py-2 rounded"
          >
            Browse Workflows
          </Link>
          <Link
            href="/tools"
            className="border border-brand text-brand px-5 py-2 rounded"
          >
            Explore Tools
          </Link>
        </div>
      </section>

      <section className="mt-10">
        <h2 className="text-2xl font-semibold mb-4">Featured Workflows</h2>
        <div className="grid md:grid-cols-2 gap-4">
          {workflows.map((w) => (
            <Link
              key={w.slug}
              href={`/workflows/${w.slug}`}
              className="block border rounded-lg p-4 hover:shadow bg-white"
            >
              <h3 className="font-bold text-brand">{w.name}</h3>
              <p className="text-sm text-slate-600 mt-1">{w.problem}</p>
              <p className="text-xs text-slate-400 mt-2">
                {w.difficulty} · saves {w.time_saved}
              </p>
            </Link>
          ))}
        </div>
      </section>

      <section className="mt-10">
        <h2 className="text-2xl font-semibold mb-4">Featured Tools</h2>
        <div className="grid md:grid-cols-3 gap-4">
          {tools.map((t) => (
            <Link
              key={t.slug}
              href={`/tools/${t.slug}`}
              className="block border rounded-lg p-4 hover:shadow bg-white"
            >
              <h3 className="font-bold">{t.name}</h3>
              <p className="text-sm text-slate-600 mt-1">{t.description}</p>
            </Link>
          ))}
        </div>
      </section>
    </div>
  );
}