import fs from "fs";
import path from "path";
import matter from "gray-matter";
import { remark } from "remark";
import remarkHtml from "remark-html";

const CONTENT_DIR = path.join(process.cwd(), "content");

export interface MarkdownDoc {
  slug: string;
  frontmatter: Record<string, unknown>;
  contentHtml: string;
}

function readMarkdownFile(folder: string, slug: string): string {
  const filePath = path.join(CONTENT_DIR, folder, `${slug}.md`);
  return fs.readFileSync(filePath, "utf8");
}

export async function getMarkdownDoc(
  folder: string,
  slug: string
): Promise<MarkdownDoc> {
  const raw = readMarkdownFile(folder, slug);
  const { data, content } = matter(raw);
  const processed = await remark().use(remarkHtml).process(content);
  return {
    slug,
    frontmatter: data,
    contentHtml: processed.toString(),
  };
}

export function listMarkdownSlugs(folder: string): string[] {
  const dir = path.join(CONTENT_DIR, folder);
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir)
    .filter((f) => f.endsWith(".md"))
    .map((f) => f.replace(/\.md$/, ""));
}