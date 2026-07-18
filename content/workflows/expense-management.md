# Workflow: Automate Expense Management

## 1. Accounting Objective
Track and categorize business expenses accurately while maintaining proper supporting documentation and tax compliance.

## 2. Accounting Process Mapping
Accounting Principles & Regulations → Expense Cycle → Expense Capture → AI Assistance → Tools & Automation

## 3. Business Problem
Kế toán nhận chi phí từ nhiều nguồn (hóa đơn, bảng kê, chi tiêu nhỏ) và phải phân loại thủ công mất ~1.5 giờ/ngày, dễ nhầm tài khoản chi phí và sót chứng từ.

## 4. Current Manual Process
```
Chi phí phát sinh → hóa đơn/phiếu chi → phân loại tay → nhập Excel → kiểm tra thuế
```
~1.5 giờ/ngày.

## 5. AI-assisted Workflow
```
Hóa đơn nhận → ChatGPT phân loại chi phí → Excel template → Kế toán review cuối
```
~20 phút/ngày.

## 6. Accounting Control Points
- Expense category: đúng tài khoản chi phí (TK 621, 622, 627, 641, 642...)
- Supporting documents: hóa đơn hợp lệ, phiếu chi, hợp đồng
- VAT deductibility: phân biệt chi phí được khấu trừ / không được khấu trừ
- Authorization: chi phí trên một ngưỡng phải có phê duyệt trước

## 7. Human Review Checklist
Before applying AI output:
- ☐ Confirm expense categorisation (Nợ đúng tài khoản chi phí)
- ☐ Check supporting documents đầy đủ và hợp lệ
- ☐ Review unusual amounts or patterns
- ☐ Approve and assign to correct cost center

## 8. Tools
| Công việc | Tool |
|-----------|------|
| Phân loại chi phí | ChatGPT |
| Trích xuất hóa đơn | Docsumo |
| Nhập liệu nhanh | Microsoft Copilot |
| Tự động hóa | Zapier |

## 9. Example Prompts
```
Prompt 1 (classify): "Phân loại chi phí sau vào tài khoản TT200: mua văn
phòng phẩm, chi phí tiếp khách, mua máy in. Trả về JSON với tài khoản Nợ/Có."

Prompt 2 (tax): "Chi phí tiếp khách 5 triệu có được khấu trừ thuế GTGT
đầu vào không? Điều kiện kèm theo nếu có."
```

## 10. Template
- `expense-tracker-template.xlsx` — bảng theo dõi chi phí + công thức tự động phân loại (free)

## 11. AI Limitations
- AI chỉ gợi ý tài khoản dựa trên mô tả — người dùng cần kiểm tra với thông tư hiện hành
- Không tự động kiểm tra hóa đơn giả
- Không thay thế quyết định cuối cùng của kế toán về phân loại chi phí

## 12. Expected Time Saving
~1h10m/day (từ 1.5h → 20 phút) khi xử lý 20-30 khoản chi phí/ngày.
