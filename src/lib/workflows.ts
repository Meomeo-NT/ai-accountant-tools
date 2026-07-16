import workflowsData from "../../data/workflows.json";

export interface Workflow {
  name: string;
  slug: string;
  difficulty: string;
  time_saved: string;
  problem: string;
  old_way: string;
  new_way: string;
  steps: string[];
  tools: string[];
  target_user: string[];
  industry: string[];
  free_template: boolean;
  seo_keywords: string[];
}

export function getAllWorkflows(): Workflow[] {
  return workflowsData as Workflow[];
}

export function getWorkflowBySlug(slug: string): Workflow | undefined {
  return getAllWorkflows().find((w) => w.slug === slug);
}