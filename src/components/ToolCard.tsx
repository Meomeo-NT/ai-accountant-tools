import Link from "next/link";
import type { Tool } from "@/lib/tools";

export default function ToolCard({ tool }: { tool: Tool }) {
  return (
    <Link
      href={`/tools/${tool.slug}`}
      className="block border rounded-lg p-5 bg-white hover:shadow"
    >
      <div className="flex justify-between items-start">
        <h2 className="text-xl font-bold">{tool.name}</h2>
        <span className="text-xs bg-slate-100 px-2 py-1 rounded">
          {tool.category}
        </span>
      </div>
      <p className="text-sm text-slate-600 mt-2">{tool.description}</p>
      <p className="text-xs text-slate-400 mt-3">
        {"★".repeat(tool.rating)}
      </p>
    </Link>
  );
}