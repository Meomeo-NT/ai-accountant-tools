"use client";

/**
 * Email capture form for lead magnet.
 *
 * Uses Formspree (formspree.io) — works with static export,
 * no server/API route needed.
 *
 * Replace FORMSPREE_ENDPOINT with your real Formspree URL after
 * registering at https://formspree.io
 */
const FORMSPREE_ENDPOINT = "https://formspree.io/f/YOUR_FORM_ID";

export default function EmailCaptureForm() {
  return (
    <form
      action={FORMSPREE_ENDPOINT}
      method="POST"
      className="mt-6 bg-brand/5 border border-brand/20 rounded-lg p-5"
    >
      <p className="text-sm font-medium text-brand">
        📥 Nhận file PDF 10 ChatGPT Prompts cho kế toán — miễn phí.
      </p>
      <div className="mt-3 flex flex-col sm:flex-row gap-2">
        <input
          type="email"
          name="email"
          placeholder="Email của bạn"
          required
          className="flex-1 px-3 py-2 border rounded text-sm"
        />
        <button
          type="submit"
          className="bg-brand text-white px-5 py-2 rounded text-sm whitespace-nowrap"
        >
          Gửi cho tôi
        </button>
      </div>
      <p className="mt-2 text-xs text-slate-400">
        Không spam. Hủy bất cứ lúc nào.
      </p>
    </form>
  );
}
