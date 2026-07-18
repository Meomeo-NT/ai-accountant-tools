import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Privacy Policy — AI Accountant Tools",
  description:
    "How we collect and handle your data. We use Formspree to process email submissions.",
};

export default function PrivacyPage() {
  return (
    <div className="max-w-2xl mx-auto">
      <h1 className="text-3xl font-bold text-brand">Privacy Policy</h1>

      <section className="mt-6 space-y-4 text-sm text-slate-700 leading-relaxed">
        <p>
          <strong>AI Accountant Tools</strong> tôn trọng quyền riêng tư của bạn.
          Trang này giải thích cách chúng tôi thu thập, sử dụng và bảo vệ thông
          tin cá nhân khi bạn sử dụng website.
        </p>

        <h2 className="text-lg font-semibold text-brand mt-6">1. Thông tin chúng tôi thu thập</h2>
        <p>
          Chúng tôi chỉ thu thập thông tin bạn tự nguyện cung cấp qua form đăng
          ký email (trang Templates): <strong>địa chỉ email</strong> của bạn.
          Chúng tôi không thu thập bất kỳ thông tin cá nhân nào khác.
        </p>

        <h2 className="text-lg font-semibold text-brand mt-6">2. Cách chúng tôi sử dụng thông tin</h2>
        <p>Email của bạn được sử dụng để:</p>
        <ul className="list-disc list-inside">
          <li>Gửi tài liệu miễn phí bạn yêu cầu (file PDF 10 ChatGPT Prompts)</li>
          <li>Thông báo nội dung mới (workflow, template) nếu bạn đồng ý</li>
        </ul>

        <h2 className="text-lg font-semibold text-brand mt-6">3. Bên thứ ba xử lý dữ liệu</h2>
        <p>
          Form đăng ký email được xử lý bởi{' '}
          <a
            href="https://formspree.io"
            target="_blank"
            rel="noopener noreferrer"
            className="text-brand underline"
          >
            Formspree
          </a>
          — một dịch vụ thu thập form bên thứ ba. Dữ liệu của bạn được lưu trữ
          trên máy chủ của Formspree và không được chia sẻ với bất kỳ bên nào
          khác. Bạn có thể xem chính sách bảo mật của Formspree tại{' '}
          <a
            href="https://formspree.io/legal/privacy-policy/"
            target="_blank"
            rel="noopener noreferrer"
            className="text-brand underline"
          >
            formspree.io/legal/privacy-policy
          </a>.
        </p>

        <h2 className="text-lg font-semibold text-brand mt-6">4. Quyền của bạn</h2>
        <p>Bạn có quyền:</p>
        <ul className="list-disc list-inside">
          <li>Yêu cầu xóa dữ liệu cá nhân của mình bất cứ lúc nào</li>
          <li>Hủy đăng ký nhận email (mỗi email đều có link hủy ở cuối)</li>
          <li>Liên hệ để biết thông tin chi tiết về dữ liệu chúng tôi đang lưu trữ</li>
        </ul>
        <p>
          Để thực hiện các quyền này, vui lòng gửi email qua form ở trang{' '}
          <Link href="/templates" className="text-brand underline">
            Templates
          </Link>{' '}
          kèm yêu cầu cụ thể.
        </p>

        <h2 className="text-lg font-semibold text-brand mt-6">5. Cookies</h2>
        <p>
          Trang web này không sử dụng cookies theo dõi. Chúng tôi không cài đặt
          bất kỳ cookie nào để thu thập thông tin cá nhân của bạn.
        </p>

        <h2 className="text-lg font-semibold text-brand mt-6">6. Thay đổi chính sách</h2>
        <p>
          Chúng tôi có thể cập nhật chính sách này theo thời gian. Mọi thay đổi
          sẽ được đăng tại trang này.
        </p>

        <p className="text-xs text-slate-400 mt-8">
          Cập nhật lần cuối: 18/07/2026
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
