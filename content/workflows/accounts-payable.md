# Workflow: Automate Accounts Payable

## 1. Accounting Objective
Manage supplier invoices from receipt to payment approval while maintaining accurate records, timely payments, and proper internal controls.

## 2. Accounting Process Mapping
Accounting Principles & Regulations → Accounts Payable Cycle → Invoice Receipt → Approval → Payment → AI Assistance → Tools & Automation

## 3. Business Problem
Kế toán phải xử lý toàn bộ vòng đời hóa đơn đầu vào: nhận, kiểm tra, duyệt, hẹn thanh toán, ghi sổ. Mỗi tháng ~100-200 hóa đơn, dễ sót hạn thanh toán, nhập trùng, và mất kiểm soát công nợ.

## 4. Current Manual Process
```
Nhận hóa đơn → nhập tay → duyệt thủ công → hẹn thanh toán Excel → ghi sổ
```
~3 giờ/ngày.

## 5. AI-assisted Workflow
```
Hóa đơn → OCR trích xuất → AI kiểm tra tính hợp lệ → Zapier gửi duyệt → Ghi sổ tự động
```
~30 phút/ngày.

## 6. Accounting Control Points
- Three-way match: hóa đơn ⇔ PO ⇔ phiếu nhập kho
- Approval routing: hóa đơn vượt ngưỡng phải được cấp thẩm quyền duyệt
- Payment terms: theo dõi hạn thanh toán để tránh phạt quá hạn
- Debit/Credit balance: kiểm soát công nợ nhà cung cấp

## 7. Human Review Checklist
Before applying AI output:
- ☐ Verify three-way match (PO + receipt note + invoice)
- ☐ Confirm GL coding (Nợ/Có đúng tài khoản)
- ☐ Check approval chain đã đầy đủ
- ☐ Review aging report (công nợ quá hạn)

## 8. Tools
| Công việc | Tool |
|-----------|------|
| Trích xuất hóa đơn OCR | Docsumo |
| Kiểm tra tính hợp lệ | ChatGPT |
| Luồng duyệt tự động | Zapier |
| Excel template theo dõi | Microsoft Copilot |

## 9. Example Prompts
```
Prompt 1 (validate): "Kiểm tra 3 matching: hóa đơn số 123, PO số 456,
phiếu nhập số 789. Các trường khớp không? Liệt kê lệch nếu có."

Prompt 2 (aging): "Từ danh sách công nợ sau, cảnh báo các hóa đơn quá
hạn thanh toán trên 30 ngày và đề xuất thứ tự ưu tiên thanh toán."
```

## 10. Template
- `ap-tracker-template.xlsx` — theo dõi toàn bộ hóa đơn đầu vào + cảnh báo hạn thanh toán (free)

## 11. AI Limitations
- Three-way match tự động chỉ khả thi khi có PO điện tử — với PO giấy vẫn cần đối chiếu thủ công
- AI không thể xác thực chữ ký trên hóa đơn giấy
- Không thay thế quyết định phê duyệt thanh toán — người có thẩm quyền vẫn là người duyệt cuối

## 12. Expected Time Saving
~2h30m/day (từ 3h → 30 phút) cho kế toán xử lý 100-200 hóa đơn đầu vào/tháng.
