# Lab 02 - Phân tích yêu cầu & Thiết kế Use Case

## 👥 Thành viên nhóm
- Họ tên 1 – Võ Nguyễn Hà Giang (leader)
- Họ tên 2 – Nguyễn Lê Tường Vi
- Họ tên 3 – Phạm Thị Tâm Như

**Mini Project:** Hệ thống quản lý đặt phòng khách sạn

## Sơ đồ Use Case
- **Use Case Diagram**: ![Use Case](diagrams/LAB2_Use case UML.jpg )
- **Sequence Diagram**: ![Sequence A](diagrams/LAB2_Sequence UML(a).jpg) ![Sequence B](diagrams/LAB2_Sequence UML(b).jpg)
- **ERD (Entity Relationship Diagram)**: ![ERD](diagrams/ERD.ipg)

## Các Use Case Description
- [UC Đặt phòng](usecases/UC_DatPhong.md)
- [UC Thanh toán](usecases/UC_ThanhToan.md)

## Use Case Descriptions (Tóm tắt)

### 1. Đặt phòng (Book Room)
**Mô tả:** Khách hàng đặt phòng khách sạn thông qua hệ thống.  
**Tác nhân:** Khách hàng.  
**Dòng sự kiện chính:**  
1. Chọn ngày nhận và trả phòng.  
2. Xem danh sách phòng trống.  
3. Chọn phòng.  
4. Hệ thống lưu thông tin và tạo hóa đơn tạm.  
5. Khách hàng xác nhận.  

---

### 2. Thanh toán (Payment)
**Mô tả:** Khách hàng thanh toán cho đơn đặt phòng.  
**Tác nhân:** Khách hàng, Nhân viên lễ tân.  
**Dòng sự kiện chính:**  
1. Chọn phương thức thanh toán.  
2. Hệ thống ghi nhận thanh toán.  
3. Nhân viên lễ tân (nếu có) xác nhận.  
4. Hệ thống cập nhật trạng thái thành “Đã thanh toán”.  
