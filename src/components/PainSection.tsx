import PainCard from "./PainCard";

const painPoints = [
  {
    icon: "📄",
    pain: "Hóa đơn PDF chất lượng kém",
    consequence:
      "Scan mờ, chụp nghiêng, chữ nhỏ — phải đọc từng ký tự, gõ tay vào Excel. Dễ sai MST, sai số hóa đơn. Mỗi lần sai mất thêm 5-10 phút dò lại.",
    solution:
      "Hướng dẫn dùng Docsumo để trích xuất nhanh các trường trên hóa đơn, kèm prompt ChatGPT tự động kiểm tra đối chiếu sau OCR — giảm thao tác gõ tay, không lo nhầm số.",
  },
  {
    icon: "🔢",
    pain: "Kiểm tra số học thủ công",
    consequence:
      "Phải bấm máy tính hoặc kéo Excel kiểm tra lại từng tờ: tổng tiền có bằng tiền hàng + thuế không? Lệch 1 đồng cũng phải dò lại từ đầu.",
    solution:
      "Prompt ChatGPT sẵn có — paste hóa đơn vào, AI tự kiểm tra biểu thức và báo lỗi nếu có. Bạn chỉ cần review kết quả, không cần tự bấm từng tờ.",
  },
  {
    icon: "🧾",
    pain: "Phân loại chi phí sai tài khoản",
    consequence:
      "Văn phòng phẩm, tiếp khách, máy tính — hạch toán vào đâu theo TT200/TT133? Sai tài khoản → kiểm toán bắt bẻ, cuối năm điều chỉnh hàng loạt.",
    solution:
      "Prompt ChatGPT gợi ý định khoản dựa trên mô tả nghiệp vụ, kèm checklist đối chiếu để bạn xác nhận trước khi ghi sổ. Bạn là người quyết định cuối cùng.",
  },
  {
    icon: "🔁",
    pain: "Nhập trùng hóa đơn",
    consequence:
      "Cùng một hóa đơn gửi qua email và giấy — hoặc hai người cùng nhập. Đến cuối kỳ mới phát hiện, phải lội sổ tìm và xóa bút toán, mất thêm 30 phút mỗi lần.",
    solution:
      "Checklist kiểm soát gợi ý các bước rà soát trùng lặp trước khi ghi sổ, hướng dẫn dùng Excel conditional formatting. Chưa có auto-detect, nhưng quy trình có sẵn giúp bạn không bỏ sót.",
  },
  {
    icon: "📅",
    pain: "Deadline báo cáo cuối kỳ",
    consequence:
      "Ngày 30 hàng tháng — vừa nhập liệu vừa lo trễ hạn nộp tờ khai. Áp lực thời gian dễ dẫn đến sai sót, bỏ sót bút toán, cuối quý càng căng thẳng.",
    solution:
      "Checklist month-end closing có sẵn — liệt kê đầy đủ các bước cần làm, ước tính thời gian từng bước, giúp không sót việc dù đang gấp.",
  },
  {
    icon: "👥",
    pain: "Phê duyệt & kiểm soát nội bộ",
    consequence:
      "Hóa đơn lớn không ai ký duyệt, người nhập cũng là người ghi sổ — thiếu tách biệt nhiệm vụ, rủi ro gian lận, kiểm toán ghi nhận điểm yếu kiểm soát.",
    solution:
      "Hướng dẫn thiết lập luồng duyệt bằng Zapier (gửi thông báo email/Slack khi hóa đơn vượt ngưỡng) kèm checklist segregation of duties để bạn tự đánh giá.",
  },
];

export default function PainSection() {
  return (
    <section className="mt-12">
      <h2 className="text-2xl font-bold mb-2 text-brand">
        Những điểm ngẽn kế toán nào AI có thể giúp?
      </h2>
      <p className="text-sm text-slate-500 mb-6">
        Theo khảo sát quốc tế của{" "}
        <a
          href="https://www.wolterskluwer.com/en/knowledge/future-ready-accountant"
          target="_blank"
          rel="noopener noreferrer"
          className="underline hover:text-brand"
        >
          Wolters Kluwer (Future Ready Accountant Report)
        </a>
        , tỷ lệ ứng dụng AI tại các hãng kế toán tăng từ 9% lên 41% chỉ trong 1
        năm. Một nghiên cứu khác của{" "}
        <a
          href="https://www.journalofaccountancy.com/news/2025/ai-adoption-accounting-closing-books.html"
          target="_blank"
          rel="noopener noreferrer"
          className="underline hover:text-brand"
        >
          Journal of Accountancy
        </a>{" "}
        trên 277 kế toán viên cho thấy nhóm dùng AI hỗ trợ đóng sổ cuối tháng
        hoàn thành nhanh hơn trung bình 7.5 ngày so với quy trình thủ công. Đây
        là số liệu quốc tế, mang tính tham khảo — kết quả thực tế tùy thuộc quy
        trình và công cụ mỗi nơi áp dụng.
      </p>
      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
        {painPoints.map((p, i) => (
          <PainCard key={i} {...p} />
        ))}
      </div>
      <div className="mt-8 text-center bg-slate-50 border rounded-lg p-6">
        <p className="text-sm text-slate-700 font-medium">
          Mỗi card trên đều có hướng dẫn cụ thể trong thư viện workflow và
          prompt của chúng tôi — hoàn toàn miễn phí, không cần đăng ký.
        </p>
        <div className="mt-4 flex justify-center gap-3">
          <a
            href="/workflows"
            className="bg-brand text-white px-5 py-2 rounded text-sm"
          >
            Xem tất cả Workflows
          </a>
          <a
            href="/templates"
            className="border border-brand text-brand px-5 py-2 rounded text-sm"
          >
            Templates & Prompts
          </a>
        </div>
      </div>
    </section>
  );
}
