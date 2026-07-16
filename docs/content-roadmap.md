# Content Roadmap — AI Accountant Tools (v2)

Tài liệu định hướng mở rộng nội dung cho AI agent / Cline sau này.
Nguyên tắc: **10 workflow sâu > 100 bài mỏng**. Mọi workflow phải tuân thủ Trust Layer.

## Phân bổ 100 trang đầu
- **40 Workflows** (tài sản cốt lõi)
- **30 Tools** (review ngắn, có affiliate)
- **20 Templates** (Excel, prompts, checklists)
- **10 Comparisons** (SEO)

## Cấu trúc thư mục content/
```
content/
├── workflows/      # /workflows/<slug>.md
├── tasks/          # /tasks/<slug>.md
├── tools/          # /tools/<slug>.md
├── templates/      # /templates/<slug>.md
├── comparisons/    # /comparisons/<slug>.md
├── use-cases/      # /use-cases/<slug>.md
└── prompts/        # /prompts/<slug>.md  (Prompt Library Strategy)
```

## Layered Model (xương sống)
```
Accounting Principles & Regulations
        ↓
Accounting Process
        ↓
Accounting Tasks
        ↓
AI Assistance
        ↓
Tools & Automation
```
AI đứng sau quy trình, không đứng trước luật.

## Workflow Content Template (bắt buộc 10 mục)
Thứ tự: **Control Points & Human Review đứng trước Tools**.
1. Accounting Objective
2. Accounting Process Mapping
3. Business Problem
4. Current Manual Process
5. AI-assisted Workflow
6. **Accounting Control Points**
7. **Human Review Checklist**
8. Tools
9. Example Prompts
10. Template
11. AI Limitations
12. Expected Time Saving

Quality rule — mọi workflow phải trả lời:
- What accounting problem?
- Which process step?
- Where can AI help?
- Where must human judgement remain?

## Trust Layer (bắt buộc mỗi workflow)
- **Accounting Control Points**: VAT treatment, expense classification, approval, segregation of duties.
- **Human Review Checklist**:
  - ☐ Verify source document
  - ☐ Confirm accounting treatment
  - ☐ Review unusual cases
  - ☐ Approve final entry
- **AI Limitations**: OCR sai trường, hiểu sai ngữ cảnh, không thay thế chuyên môn.

## 10 Workflow ưu tiên (sâu, theo template trên)
1. invoice-processing ✅ (đã chuẩn hóa 12 sections)
2. bank-reconciliation ✅
3. month-end-closing ✅
4. expense-management
5. financial-reporting
6. tax-preparation
7. excel-automation
8. data-analysis
9. audit-testing
10. accounts-payable

## Prompt Library Strategy
Thêm `content/prompts/`:
- invoice-prompts.md
- reconciliation-prompts.md
- reporting-prompts.md
Tài sản bán được (gói SOP Pack).

## Template ưu tiên
- invoice-entry-template.xlsx
- bank-reconciliation-template.xlsx
- month-end-closing-checklist
- 100 ChatGPT prompts (Starter Pack $19) · SOP Pack $29

## Use Cases ưu tiên
- sme-accountant ✅
- manufacturing-accountant
- retail-accountant
- service-accountant
- startup-accountant

## Accounting Framework (phạm vi)
Framework phục vụ automation, KHÔNG thay chuẩn mực.
- Invoice Accounting · Revenue Recognition · Fixed Assets · Inventory · Expense · Financial Reporting
- Liên kết: Framework → Process → Task → AI Automation → Tool

## Global-first Strategy (phễu locale)
- **Phase 1:** Global accounting workflows (invoice, reconciliation, closing…)
- **Phase 2:** Regional accounting guides
- **Phase 3:** Vietnam accounting module (TT200, TT133, Tax)
VN là layer sau, tránh rủi ro sai luật sớm.

## Tiêu chí SEO
- Từ khóa dài: "how accountants automate X", "AI for X accounting"
- Mỗi trang có `seo_keywords` trong data JSON tương ứng.
- Tránh cạnh tranh từ khóa ngắn ("ChatGPT", "AI tools").

## Khi nào build website
Chỉ build Next.js static export SAU khi có ≥10 workflows chuẩn (theo template 10 mục) + 20 tools + 5 templates.
Thứ tự: Product Foundation → 10 Workflows → 20 Tools → 5 Templates → Website → SEO → Affiliate + SOP Pack.

## Công việc còn lại
- [ ] TODO: content/free-resources/ folder — planned lead-magnet section (not built yet)