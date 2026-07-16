import Link from "next/link";

export default function NotFound() {
  return (
    <div className="text-center py-20">
      <h1 className="text-3xl font-bold text-brand">404 — Not found</h1>
      <p className="mt-4 text-slate-600">
        The page you are looking for does not exist.
      </p>
      <Link href="/" className="text-brand underline mt-4 inline-block">
        Back to home
      </Link>
    </div>
  );
}