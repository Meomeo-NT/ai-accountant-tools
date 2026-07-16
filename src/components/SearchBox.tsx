export default function SearchBox() {
  return (
    <div className="w-full max-w-md mx-auto">
      <input
        type="search"
        placeholder="Search AI tools for accountants…"
        disabled
        className="w-full border rounded px-4 py-2 text-sm bg-slate-100 cursor-not-allowed"
        aria-label="Search (coming soon)"
      />
      <p className="text-xs text-slate-400 mt-1 text-center">
        Search coming soon
      </p>
    </div>
  );
}