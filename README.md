# AI Accountant Tools — Smart Accounting Toolkit

> *"Tools, templates and AI workflows that help accountants work faster."*

Đây là **Product Vision Document** (không phải tài liệu kỹ thuật). Dự án chưa xây website — bước hiện tại là tạo **Product Foundation**: cấu trúc nội dung, schema dữ liệu và bộ khung content. Website static (Next.js) chỉ được dựng SAU khi có nội dung đúng.

---

## 1. Problem (Vấn đề)

Hàng triệu kế toán viên trên thế giới dành hàng giờ mỗi ngày cho công việc lặp lại:
- Nhập tay hóa đơn từ PDF / email
- Đối chiếu công nợ, ngân hàng thủ công
- Tổng hợp báo cáo cuối tháng trên Excel
- Kiểm tra số liệu, định dạng báo cáo, gửi email

Họ không cần "thêm một AI tool nữa". Họ cần câu trả lời cho:
> *"Tôi đang mất 3 tiếng làm báo cáo, có cách nào nhanh hơn không?"*

## 2. Solution (Giải pháp)

Một **thư viện thực tế** (không phải directory copy dữ liệu) cho thấy AI có thể tự động hóa công việc kế toán hàng ngày như thế nào — qua **workflow** cụ thể có before/after, tool gợi ý, prompt mẫu và template tải về.

Bản chất dự án = **Wikipedia + Blog chuyên ngành + Affiliate marketplace + Knowledge base**.
Tài sản chính không phải code, mà là:
- 100 workflow kế toán thực tế
- 100 tool review
- 100 bài SEO

Code chỉ là cái khung.

## 3. AI Philosophy & Compliance Principle (Triết lý & Tuân thủ)

### AI Assistant, not AI Accountant
AI là **trợ lý**, không phải kế toán trưởng. AI đứng sau quy trình, không đứng trước luật.

### Compliance Principle (bắt buộc)
- *AI does not replace accounting judgment or regulatory compliance. It helps accountants automate repetitive tasks while keeping professional standards and internal controls.*
- *AI recommendations should always be reviewed by qualified accounting professionals before being applied to financial records.*

### Layered Model (xương sống triết lý)
```
Accounting Principles & Regulations   (không đổi)
        ↓
Accounting Process                     (không đổi)
        ↓
Accounting Tasks                       (công việc hàng ngày)
        ↓
AI Assistance                          (giảm thao tác, không quyết định)
        ↓
Tools & Automation
```
Ví dụ Việt Nam chỉ là một layer sau này: `Vietnam Accounting Regulations` (TT200, TT133, Thuế).

## 4. Information Architecture (IA)

```
Home
 ├── Workflows ⭐⭐⭐⭐⭐   (tài sản SEO chính)
 ├── Accounting Tasks
 ├── Accounting Framework   (Knowledge Base phục vụ automation, chưa build ngay)
 ├── Tools
 ├── Templates
 ├── Free Resources ⭐      (lead magnet → email list)
 ├── Use Cases              (theo hoàn cảnh: SME, thương mại, sản xuất…)
 └── Comparisons           (ChatGPT vs Claude, Excel Copilot vs ChatGPT…)
```

Luồng: **Tools → Workflows → Comparisons → Affiliate** (không phải Tools → Affiliate).

### Accounting Framework (phạm vi rõ)
Framework phục vụ **automation**, không thay thế chuẩn mực. Không viết "Chuẩn mực hàng tồn kho là gì?" mà viết "Inventory accounting workflow và điểm AI hỗ trợ".
Liên kết: `Framework → Process → Task → AI Automation → Tool`.

## 5. Scope Boundary (Giới hạn phạm vi)

- ❌ Không tự động hóa quyết định kế toán (định khoản, thuế, báo cáo) thay con người.
- ❌ Không cung cấp tư vấn pháp lý / thuế thay cho chuyên gia.
- ❌ Không cam kết số liệu đầu ra chính xác 100% không cần kiểm tra.
- ✅ Chỉ hỗ trợ giảm thao tác thủ công (OCR, nhập liệu, draft, tóm tắt).
- ✅ Mọi output AI phải qua **Human Review Checklist** trước khi ghi sổ.
- ✅ Tuân thủ quy trình, chuẩn mực và kiểm soát nội bộ hiện hành.

## 6. Data Schema (mở rộng)

Lưu tại `data/*.json`. Không cần database.

### data/tools.json
```json
{
  "name": "ChatGPT",
  "slug": "chatgpt",
  "category": "Financial Analysis",
  "description": "AI assistant for financial analysis, reporting and spreadsheet explanations.",
  "pricing": "Free / Plus",
  "rating": 5,
  "target_user": ["Accountant", "SME Finance Team", "Financial Analyst"],
  "industry": ["Retail", "Manufacturing", "Service"],
  "problems": ["Report writing", "Data analysis", "Excel formula"],
  "affiliate_url": "YOUR_AFFILIATE_LINK",
  "affiliate_network": "OpenAI",
  "seo_keywords": ["AI for financial reporting", "AI Excel assistant"]
}
```

### data/tasks.json / data/workflows.json
```json
{
  "name": "Invoice Processing",
  "slug": "invoice-processing",
  "difficulty": "Beginner",
  "time_saved": "2 hours/week",
  "old_way": "Manual PDF entry",
  "new_way": "AI OCR + validation",
  "tools": ["ChatGPT", "Docsumo", "Microsoft Copilot", "Zapier"],
  "target_user": ["Accountant", "SME Finance Team"],
  "industry": ["Retail", "Manufacturing", "Service"],
  "free_template": true
}
```

**Lợi ích 4 field mới:** tạo filter `Beginner/Intermediate/Advanced`, `AI tools for manufacturing accountants`, `AI tools for SME accountants` — mà không sửa cấu trúc.

## 7. Content Plan — 100 trang đầu (ưu tiên chất lượng)

- **40 Workflows** (tài sản) · **30 Tools** · **20 Templates** · **10 Comparisons**
- Nguyên tắc: **10 workflow sâu > 100 bài mỏng**.

### Workflow Content Template (bắt buộc 10 mục — Control Points & Human Review đứng trước Tools)
1. Accounting Objective
2. Business Problem
3. Current Manual Process
4. AI-assisted Process
5. **Accounting Control Points**
6. **Human Review Checklist**
7. Tools
8. Example Prompt
9. Template
10. Limitations

Mọi workflow phải trả lời: *What accounting problem? Which process step? Where can AI help? Where must human judgement remain?*

## 8. Free Resources (điểm kiếm tiền sớm)

- Free: *10 ChatGPT prompts for accountants* → thu email.
- Sau này: *Accounting AI Starter Pack* $19 (100 prompts + 50 Excel templates + 20 automation workflows).
- Email list = tài sản dài hạn.

## 9. Business Model & Affiliate Tracking

Không cần backend. Chuẩn bị sẵn trong `tools.json`: `affiliate_url` + `affiliate_network`.

### Monetization (thứ tự ưu tiên)
1. **Accounting AI SOP Pack — $29** (đẩy sớm hơn affiliate): Month-end closing checklist + AI prompts + Excel templates + automation guide. Với 1000 visitor/tháng, giữ 50 email → bán 2 gói ≈ $58 (khả thi hơn affiliate).
2. **Digital product**: Starter Pack $19, mini-course $49.
3. **Affiliate**: AI subscription, OCR, accounting SaaS, cloud, automation.
4. **Sponsored listing** ($100/tháng sau có traffic).
5. **Newsletter sponsor**.

## 10. Roadmap

- **Phase 1 (7 ngày):** Website có giá trị — 10 workflows chuẩn + 20 tools + 5 templates.
- **Phase 2 (30 ngày):** 50 workflows + 100 tools + Google index + first affiliate clicks.
- **Phase 3 (90 ngày):** Newsletter + Digital product + Affiliate + Community.

### Thứ tự thực hiện (tránh bẫy "đẹp nhưng không content")
```
Product Foundation ✅
      ↓
10 Accounting Workflows
      ↓
20 Tools mapping
      ↓
5 Templates
      ↓
Next.js static website
      ↓
SEO deployment
      ↓
Affiliate + SOP Pack
```

## 11. Success Metrics

| Giai đoạn | Chỉ số |
|-----------|--------|
| Tháng 1 | 50 indexed pages · 100 organic visitors |
| Tháng 3 | 1000 visitors/month · First affiliate conversion |
| Tháng 6 | $100–$500/month revenue |

## 12. Tech (sẽ dùng khi build website)

- Next.js 15 static export, Tailwind, App Router
- Không DB, không backend, không login
- Deploy Vercel / Cloudflare Pages — chi phí $0
- Data đọc từ `data/*.json` + markdown trong `content/`

---
*Trạng thái hiện tại: Product Foundation (v2) — đã có Compliance Principle, Trust Layer, Scope Boundary. Chưa có code Next.js.*