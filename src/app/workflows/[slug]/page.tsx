import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { getAllWorkflows, getWorkflowBySlug } from "@/lib/workflows";
import { getMarkdownDoc } from "@/lib/markdown";

export function generateStaticParams() {
  return getAllWorkflows().map((w) => ({ slug: w.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  const { slug } = await params;
  const w = getWorkflowBySlug(slug);
  if (!w) return { title: "Workflow not found" };
  return {
    title: `${w.name} — AI Accountant Tools`,
    description: w.problem,
    keywords: w.seo_keywords,
  };
}

export default async function WorkflowDetail({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const w = getWorkflowBySlug(slug);
  if (!w) notFound();

  const doc = await getMarkdownDoc("workflows", slug).catch(() => null);

  return (
    <article>
      <Link href="/workflows" className="text-sm text-brand">
        ← All workflows
      </Link>
      <h1 className="text-3xl font-bold text-brand mt-2">{w.name}</h1>
      <div className="flex flex-wrap gap-2 text-xs my-3">
        <span className="bg-slate-100 px-2 py-1 rounded">{w.difficulty}</span>
        <span className="bg-slate-100 px-2 py-1 rounded">
          saves {w.time_saved}
        </span>
        {w.free_template && (
          <span className="bg-green-100 px-2 py-1 rounded">
            free template
          </span>
        )}
      </div>

      <section className="mt-4 bg-white border rounded-lg p-5">
        <h2 className="font-semibold">Accounting Objective</h2>
        <p className="mt-1 text-slate-700">{w.problem}</p>
        <h2 className="font-semibold mt-4">Current vs AI-assisted</h2>
        <p className="mt-1 text-slate-700">
          <span className="line-through text-slate-400">{w.old_way}</span> →{" "}
          {w.new_way}
        </p>
        <h2 className="font-semibold mt-4">Steps</h2>
        <ol className="list-decimal ml-5 mt-1 text-slate-700">
          {w.steps.map((s, i) => (
            <li key={i}>{s}</li>
          ))}
        </ol>
      </section>

      {doc && (
        <section
          className="mt-6 prose max-w-none"
          dangerouslySetInnerHTML={{ __html: doc.contentHtml }}
        />
      )}

      <section className="mt-6 bg-white border rounded-lg p-5">
        <h2 className="font-semibold">Tools used</h2>
        <ul className="mt-2 flex flex-wrap gap-2">
          {w.tools.map((t) => (
            <li key={t} className="bg-brand text-white px-3 py-1 rounded text-sm">
              {t}
            </li>
          ))}
        </ul>
      </section>

      <p className="mt-8 text-xs text-slate-500 italic">
        AI recommendations should always be reviewed by qualified accounting
        professionals before being applied to financial records.
      </p>
    </article>
  );
}