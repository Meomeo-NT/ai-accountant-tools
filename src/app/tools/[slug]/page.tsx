import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { getAllTools, getToolBySlug, isAffiliateReady } from "@/lib/tools";

export function generateStaticParams() {
  return getAllTools().map((t) => ({ slug: t.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  const { slug } = await params;
  const t = getToolBySlug(slug);
  if (!t) return { title: "Tool not found" };
  return {
    title: `${t.name} — AI Accountant Tools`,
    description: t.description,
    keywords: t.seo_keywords,
  };
}

export default async function ToolDetail({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const t = getToolBySlug(slug);
  if (!t) notFound();

  const ready = isAffiliateReady(t.affiliate_url);

  return (
    <article>
      <Link href="/tools" className="text-sm text-brand">
        ← All tools
      </Link>
      <h1 className="text-3xl font-bold text-brand mt-2">{t.name}</h1>
      <span className="inline-block mt-2 text-xs bg-slate-100 px-2 py-1 rounded">
        {t.category}
      </span>
      <p className="mt-4 text-slate-700">{t.description}</p>

      <section className="mt-4 bg-white border rounded-lg p-5">
        <h2 className="font-semibold">Best for</h2>
        <ul className="list-disc ml-5 mt-1 text-slate-700">
          {t.problems.map((p, i) => (
            <li key={i}>{p}</li>
          ))}
        </ul>
        <h2 className="font-semibold mt-4">Target users</h2>
        <p className="mt-1 text-slate-700">{t.target_user.join(", ")}</p>
        <h2 className="font-semibold mt-4">Industries</h2>
        <p className="mt-1 text-slate-700">{t.industry.join(", ")}</p>
        <h2 className="font-semibold mt-4">Pricing</h2>
        <p className="mt-1 text-slate-700">{t.pricing}</p>
      </section>

      <div className="mt-6">
        {ready ? (
          <a
            href={t.affiliate_url}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-block bg-brand text-white px-5 py-2 rounded"
          >
            Try {t.name} →
          </a>
        ) : (
          <span className="inline-block bg-slate-200 text-slate-500 px-5 py-2 rounded cursor-not-allowed">
            Coming soon
          </span>
        )}
      </div>

      <p className="mt-8 text-xs text-slate-500 italic">
        AI recommendations should always be reviewed by qualified accounting
        professionals before being applied to financial records.
      </p>
    </article>
  );
}