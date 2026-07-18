interface PainCardProps {
  icon: string;
  pain: string;
  consequence: string;
  solution: string;
}

export default function PainCard({ icon, pain, consequence, solution }: PainCardProps) {
  return (
    <div className="border rounded-lg p-6 bg-white hover:shadow-md transition-shadow flex flex-col">
      <div className="text-3xl mb-3">{icon}</div>
      <h3 className="font-bold text-sm uppercase tracking-wide text-accent">{pain}</h3>
      <p className="text-sm text-slate-600 mt-3 leading-relaxed">{consequence}</p>
      <div className="mt-4 pt-4 border-t border-slate-200 bg-slate-50 -mx-6 -mb-6 px-6 pb-6 rounded-b-lg">
        <p className="text-xs font-medium text-accent uppercase tracking-wide mb-1">
          ✅ Giải pháp
        </p>
        <p className="text-xs text-slate-500 leading-relaxed">{solution}</p>
      </div>
    </div>
  );
}
