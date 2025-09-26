# Lab 06 – Thiết kế chi tiết lớp & kiến trúc ATM

## Class Diagram
- **ATM**: quản lý các giao dịch, xác thực thẻ, rút/nạp/chuyển tiền.
- **Card**: thông tin thẻ, trạng thái.
- **Account**: quản lý số dư, nợ và có.
- **Transaction**: ghi lại thông tin giao dịch.

## Package Diagram
- **UI**: giao diện người dùng (màn hình, nhập liệu).
- **Controller**: điều phối luồng xử lý giao dịch.
- **BankService**: kết nối với hệ thống ngân hàng.
- **Hardware**: phần cứng (CardReader, CashDispenser, DepositSlot).

## Công cụ
- PlantUML (VS Code plugin).
- Export diagram ra PNG để nộp.

## Nộp
- `class-atm.puml` + `class-atm.png`
- `package-diagram.puml` + `package-diagram.png`
- `notes.md`
