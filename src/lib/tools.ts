import toolsData from "../../data/tools.json";

export interface Tool {
  name: string;
  slug: string;
  category: string;
  description: string;
  pricing: string;
  rating: number;
  target_user: string[];
  industry: string[];
  problems: string[];
  affiliate_url: string;
  affiliate_network: string;
  seo_keywords: string[];
}

export function getAllTools(): Tool[] {
  return toolsData as Tool[];
}

export function getToolBySlug(slug: string): Tool | undefined {
  return getAllTools().find((t) => t.slug === slug);
}

export function isAffiliateReady(url: string): boolean {
  return Boolean(url) && url !== "YOUR_AFFILIATE_LINK";
}
