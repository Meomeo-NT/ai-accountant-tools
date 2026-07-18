interface PainCardProps {
  icon: string;
  pain: string;
  consequence: string;
  solution: string;
}

export default function PainCard({ icon, pain, consequence, solution }: PainCardProps) {
  return (
    <div className="border border-slate-200 rounded-xl p-6 bg-white shadow-sm hover:shadow-md hover:border-accent/20 transition-all duration-200 flex flex-col">
      <div className="flex items-center gap-3 mb-3">
        <span className="inline-flex items-center justify-center w-12 h-12 rounded-full bg-accent/10 text-2xl">
          {icon}
        </span>
        <h3 className="font-bold text-xs uppercase tracking-wide text-accent-text">
          {pain}
        </h3>
      </div>
      <p className="text-base text-slate-700 leading-relaxed">{consequence}</p>
      <div className="mt-4 pt-4 border-t border-slate-200 bg-accent/5 -mx-6 -mb-6 px-6 pb-6 rounded-b-xl">
        <p className="text-xs font-medium text-accent-text uppercase tracking-wide mb-1">
          ✅ Giải pháp
        </p>
        <p className="text-sm text-slate-600 leading-relaxed">{solution}</p>
      </div>
    </div>
  );
}
