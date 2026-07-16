import type { MetadataRoute } from "next";

export const dynamic = "force-static";
import { getAllTools } from "@/lib/tools";
import { getAllWorkflows } from "@/lib/workflows";

export default function sitemap(): MetadataRoute.Sitemap {
  const base = "https://ai-accountant-tools.vercel.app";
  const toolRoutes = getAllTools().map((t) => ({
    url: `${base}/tools/${t.slug}`,
  }));
  const workflowRoutes = getAllWorkflows().map((w) => ({
    url: `${base}/workflows/${w.slug}`,
  }));
  return [
    { url: base },
    { url: `${base}/workflows` },
    { url: `${base}/tools` },
    { url: `${base}/templates` },
    { url: `${base}/comparisons` },
    ...toolRoutes,
    ...workflowRoutes,
  ];
}