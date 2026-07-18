interface PainCardProps {
  icon: string;
  pain: string;
  consequence: string;
  solution: string;
}

export default function PainCard({ icon, pain, consequence, solution }: PainCardProps) {
  return (
    <div className="border rounded-lg p-5 bg-white hover:shadow transition-shadow">
      <div className="text-2xl mb-2">{icon}</div>
      <h3 className="font-bold text-brand text-sm uppercase tracking-wide">{pain}</h3>
      <p className="text-sm text-slate-600 mt-2">{consequence}</p>
      <div className="mt-3 pt-3 border-t border-slate-100">
        <p className="text-xs text-slate-500 leading-relaxed">{solution}</p>
      </div>
    </div>
  );
}
