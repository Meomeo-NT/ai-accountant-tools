# Design System — AI Accountant Tools

> Tổng hợp pattern thiết kế từ Stripe, Linear, Mercury, Ramp, Puzzle
> Giữ tông xanh navy hiện tại (#1f3a5f), điều chỉnh accent + spacing

---

## 1. Bảng màu đề xuất

| Vai trò | Mã màu | Ghi chú |
|---------|--------|---------|
| **Brand primary** | `#1f3a5f` | Xanh navy — giữ nguyên (brand hiện tại) |
| **Brand light** | `#2c5282` | Xanh navy sáng hơn — giữ nguyên |
| **Accent** (bg/border/icon) | `#0d9488` | Teal — dùng cho background nhạt, border, icon fill |
| **Accent-text** (mọi text) | `#0f766e` | Teal-700 đậm hơn — WCAG AA ~5.2:1 trên nền trắng, dùng cho heading, link, label |
| **Neutral 50** | `#f8fafc` | Nền sáng nhất (giống Puzzle bg) |
| **Neutral 100** | `#f1f5f9` | Nền card (giống Ramp card bg) |
| **Neutral 200** | `#e2e8f0` | Border nhẹ |
| **Neutral 600** | `#475569` | Text secondary |
| **Neutral 900** | `#0f172a` | Text primary (đậm hơn đen pure) |
| **Background** | `#ffffff` | Nền trang |
| **Dark section** | `#0f172a` | Nền section tối (lấy từ Linear + Mercury) |

### Lưu ý contrast (WCAG AA):
- `#0d9488` trên nền trắng: ~3.4:1 — **chỉ dùng cho bg/border/icon**, không dùng làm text
- `#0f766e` trên nền trắng: ~5.2:1 — **đạt WCAG AA**, dùng cho mọi text màu accent

---

## 2. Font Pairing đề xuất

| Vai trò | Font | Fallback |
|---------|------|----------|
| **Heading** | `Inter` (sans-serif) | `system-ui, -apple-system, sans-serif` |
| **Body** | `Inter` | `system-ui, -apple-system, sans-serif` |
| **Monospace** (code) | `JetBrains Mono` | `monospace` |

### Cỡ chữ chuẩn:
- Hero heading: `text-4xl` → `text-5xl` (36-48px)
- Section heading: `text-2xl` → `text-3xl` (24-30px)
- Card title: `text-lg` → `text-xl` (18-20px)
- Body: `text-base` (16px)
- Small/caption: `text-sm` (14px)
- Label: `text-xs uppercase tracking-wide` (12px)

> **Import:** Dùng `next/font/google` trong `layout.tsx`, không link CDN trực tiếp.

---

## 3. Spacing chuẩn

| Khoảng cách | Giá trị | Tailwind class |
|-------------|---------|----------------|
| **Section gap** (giữa các section lớn) | 96px | `my-24` |
| **Section padding** (padding trong section) | 64px | `py-16` |
| **Card padding** | 24px | `p-6` |
| **Card inner gap** (giữa các element trong card) | 12-16px | `space-y-3` → `space-y-4` |
| **Grid gap** (giữa các card trong grid) | 24-32px | `gap-6` → `gap-8` |
| **Content max-width** | 1152px | `max-w-6xl mx-auto` |
| **Narrow content** (text-heavy) | 768px | `max-w-3xl mx-auto` |

### Pattern spacing từ các trang tham khảo:
- **Stripe:** Section gap rất lớn (120-160px), tạo cảm giác "premium"
- **Linear:** Section gap vừa (80-120px), phù hợp dark theme
- **Mercury:** Section gap lớn (100-140px), nhiều whitespace
- **Ramp:** Section gap vừa (80-120px), tập trung vào nội dung
- **Puzzle:** Section gap vừa (80-120px), clean professional

→ **Chọn mức trung bình: 96px (my-24) cho section gap, 64px (py-16) cho section padding**

---

## 4. Card Design

### Border
- **Default card:** `border border-slate-200` (1px, màu nhẹ)
- **Hover:** `hover:border-accent/20` (đổi màu border khi hover)
- **No border variant:** dùng bg khác để phân biệt (giống Mercury)

### Border Radius
- **Card:** `rounded-xl` (12px) — lấy từ Stripe + Ramp
- **Button:** `rounded-lg` (8px)
- **Small element:** `rounded-md` (6px)

### Shadow
- **Default:** `shadow-sm` (giống Stripe: 0 1px 2px rgba(0,0,0,0.05))
- **Hover:** `hover:shadow-md` (nâng lên khi hover)
- **Elevated card:** `shadow-md` (cho card nổi bật)

### Background
- **Light theme card:** `bg-white` (mặc định)
- **Alternate card:** `bg-slate-50` (giống Ramp card bg)
- **Dark theme card:** `bg-slate-800` (cho dark section)

---

## 5. Layout Patterns (áp dụng cho PainCard)

### Cấu trúc PainCard mới (tham khảo HyperUI marketing card):

```
┌─────────────────────────────────────┐
│  [icon]  [pain label - uppercase]   │
│                                     │
│  [consequence text - body]          │
│                                     │
│  ──── divider ────                  │
│  ✅ Giải pháp                        │
│  [solution text]                    │
└─────────────────────────────────────┘
```

### Cải tiến:
1. **Icon:** to hơn (`text-4xl`), có bg circle nhẹ
2. **Pain label:** giữ nguyên uppercase + `text-accent-text` (đậm hơn, đọc được)
3. **Consequence:** tăng `text-base`, thêm `text-slate-700`
4. **Solution section:** đổi bg thành `bg-accent/5` (màu accent siêu nhạt) thay vì `bg-slate-50`
5. **"✅ Giải pháp" label:** dùng `text-accent-text` thay vì `text-accent`
6. **Hover:** thêm hiệu ứng border chuyển màu + shadow nâng lên

---

## 6. Dark Section Pattern

Khi cần section nền tối (lấy cảm hứng từ Linear + Mercury):
- Background: `bg-slate-900` (#0f172a)
- Text primary: `text-white`
- Text secondary: `text-slate-400`
- Card trong dark section: `bg-slate-800` với `border-slate-700`

---

## 7. Button Style

| Loại | Class | Ghi chú |
|------|-------|---------|
| **Primary CTA** | `bg-accent text-white px-6 py-3 rounded-lg font-medium hover:bg-accent-light` | Dùng cho main action |
| **Secondary** | `border border-accent text-accent-text px-6 py-3 rounded-lg font-medium hover:bg-accent/5` | Dùng cho phụ — text dùng accent-text |
| **Ghost** | `text-accent-text hover:text-accent-text/80 font-medium` | Dùng cho link — text dùng accent-text |

---

## 8. Checklist áp dụng

- [x] Xác nhận content max-width: **`max-w-6xl` (1152px)** — giá trị cuối cùng
- [x] Cập nhật `tailwind.config.ts` — thêm neutral scale, accent/accent-text
- [x] Sửa `PainCard.tsx` — áp dụng card design mới
- [x] Import Inter font trong layout.tsx bằng `next/font/google`
- [x] Tăng spacing giữa các section (my-24, py-16)
- [ ] Build local test
- [ ] Push lên GitHub
