import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "About — AI Accountant Tools",
  description:
    "A personal project collecting practical ways accountants can use AI. Independent, transparent, and grounded in experience.",
};

export default function AboutPage() {
  return (
    <div className="max-w-2xl mx-auto">
      <h1 className="text-3xl font-bold text-brand">About</h1>

      <section className="mt-6 space-y-4 text-sm text-slate-700 leading-relaxed">
        <p>
          <strong>AI Accountant Tools</strong> là một dự án cá nhân — không phải
          công ty, không phải đội ngũ chuyên gia. Tôi tổng hợp những cách dùng
          AI (ChatGPT, Docsumo, Copilot...) cho các nghiệp vụ kế toán cụ thể tại
          Việt Nam, dựa trên trải nghiệm sử dụng thực tế và nghiên cứu công khai
          có nguồn.
        </p>

        <p>
          Trang này ra đời vì một lý do đơn giản: hầu hết nội dung về AI cho kế
          toán hiện nay bằng tiếng Anh, viết cho thị trường Mỹ/Âu, dùng các quy
          trình và quy định không áp dụng được ở Việt Nam. Tôi muốn có một nơi
          tập hợp các workflow, prompt và template phù hợp với kế toán Việt —
          từ TT200/TT133, hóa đơn GTGT, MST, đến các tình huống thực tế hàng
          ngày.
        </p>

        <p>
          <strong>Cách tôi chọn nội dung:</strong> mỗi workflow và tool được
          đánh giá dựa trên trải nghiệm cá nhân, không phải khảo sát chính thức
          — điều này được ghi rõ trong từng bài. Nếu tôi chưa dùng qua một
          tool, tôi không chấm điểm hay khuyến nghị nó.
        </p>

        <div className="bg-slate-50 border rounded-lg p-4 text-xs text-slate-500">
          <p className="font-medium text-slate-700">Minh bạch</p>
          <ul className="mt-2 list-disc list-inside space-y-1">
            <li>Đây là dự án cá nhân, một người làm — không có đội ngũ đánh giá chuyên nghiệp</li>
            <li>Các đánh giá tool là chủ quan, dựa trên trải nghiệm thực tế</li>
            <li>Trang có thể nhận hoa hồng từ một số link affiliate (đã ghi rõ trong footer)</li>
            <li>AI không thay thế phán đoán kế toán — mọi đề xuất cần được review bởi người có chuyên môn</li>
          </ul>
        </div>

        <p>
          Nếu có câu hỏi hoặc góp ý, bạn có thể để lại email qua form ở trang{' '}
          <Link href="/templates" className="text-brand underline">
            Templates
          </Link>
          .
        </p>
      </section>

      <p className="mt-8 text-sm">
        <Link href="/" className="text-brand underline">
          ← Back home
        </Link>
      </p>
    </div>
  );
}
