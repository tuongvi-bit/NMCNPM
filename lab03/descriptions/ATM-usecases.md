# ATM Mini Project – Use Case & Sequence

## Use Case: Rút tiền
**Tác nhân chính:** Khách hàng  
**Mục tiêu:** Khách hàng rút được số tiền mong muốn từ ATM.  

**Luồng chính:**
1. Khách hàng đưa thẻ và nhập mã PIN.
2. Hệ thống kiểm tra thông tin với Bank Server.
3. Khách hàng chọn số tiền cần rút.
4. ATM gửi yêu cầu đến Bank Server kiểm tra số dư.
5. Bank Server xác nhận và trừ tiền.
6. ATM trả tiền mặt cho khách hàng.

**Ngoại lệ:**
- Nhập sai PIN 3 lần → ATM giữ thẻ.
- Số dư không đủ → hiển thị thông báo.

---

## Sequence Diagram: Rút tiền
**Đối tượng tham gia:**  
- Khách hàng  
- ATM  
- Bank Server  

**Thông điệp trao đổi:**  
- Khách hàng ↔ ATM: Nhập PIN, chọn số tiền.  
- ATM ↔ Bank Server: Xác thực, kiểm tra số dư, cập nhật giao dịch.  
- ATM → Khách hàng: Xuất tiền + biên lai.