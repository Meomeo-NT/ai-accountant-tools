# Workflow: Automate Invoice Processing

## 1. Accounting Objective
Record supplier invoices accurately and timely while maintaining audit trail and internal controls.

## 2. Accounting Process Mapping
Accounting Principles & Regulations → Accounts Payable Process → Invoice Capture → AI Assistance → Tools & Automation

## 3. Business Problem
Kế toán nhận hóa đơn PDF/email và phải nhập tay vào Excel mất ~2 giờ/ngày, dễ sai sót OCR và nhập trùng.

## 4. Current Manual Process
```
PDF Invoice → Đọc tay từng trường → Nhập Excel → Kiểm tra lại
```
~2 giờ/ngày.

## 5. AI-assisted Workflow
```
PDF Invoice → AI OCR → ChatGPT Validate → Export Excel/SW → Kế toán review cuối
```
~15 phút/ngày.

## 6. Accounting Control Points
- VAT treatment: kiểm tra MST, thuế suất, loại hóa đơn (GTGT/Ban hang)
- Expense classification: đúng tài khoản chi phí/công nợ
- Approval: hóa đơn > ngưỡng phải có phê duyệt
- Segregation of duties: người nhập ≠ người duyệt ≠ người ghi sổ

## 7. Human Review Checklist
Before applying AI output:
- ☐ Verify source document (PDF gốc khớp dữ liệu OCR)
- ☐ Confirm accounting treatment (tài khoản Nợ/Có, thuế, phí)
- ☐ Review unusual cases (số tiền bất thường, NCC lạ)
- ☐ Approve final entry (ghi sổ sau kiểm tra)

## 8. Tools
| Công việc | Tool |
|-----------|------|
| Trích xuất dữ liệu | Docsumo |
| Kiểm tra / validate | ChatGPT |
| Nhập Excel nhanh | Microsoft Copilot |
| Tự động hóa luồng | Zapier |

## 9. Example Prompts
```
Prompt 1 (validate): "Kiểm tra hóa đơn sau: tổng = tiền hàng + thuế?
MST đủ 10 số? Ngày hợp lệ? Trả về JSON các lỗi nếu có."

Prompt 2 (account): "Gợi ý tài khoản kế toán cho hóa đơn mua văn phòng phẩm,
máy tính, chi phí tiếp khách theo TT200."
```

## 10. Template
- `invoice-entry-template.xlsx` — cột chuẩn + công thức kiểm tra tự động (free)

## 11. AI Limitations
- OCR có thể sai trường (số hóa đơn, ngày, MST) nếu PDF mờ/quét xấu
- AI không phân biệt được loại hóa đơn (GTGT thật/giả)
- Không thay thế quyết định kế toán: ghi Nợ/Có, phân loại thuế

## 12. Expected Time Saving
~1h45m/day (từ 2h → 15 phút) cho kế toán có 30-50 hóa đơn/ngày.