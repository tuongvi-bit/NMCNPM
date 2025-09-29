# Lab 09 — Quản lý dự án ATM trên Jira (Agile)

## Thông tin

* Project: **ATM System**
* Epic: **ATM Basic Functions**
* Sprint 1: Sprint 1 — Withdraw & Check Balance
* Duration: 2025-09-29 → 2025-10-13
* Team: [Điền họ tên thành viên + vai trò]

---

## Mục tiêu

Mô phỏng quản lý phát triển hệ thống ATM bằng Scrum: tạo backlog, lập sprint, giao việc, theo dõi burndown chart và lập báo cáo.

---

## Backlog (Epic & User Stories)

* **Epic:** ATM Basic Functions

**User Stories:**

1. **US1 – Rút tiền (5 SP)**
   *As a customer, I want to withdraw cash from my account so that I can use money when needed.*

   * **Acceptance Criteria:**

     * Given a valid card and PIN and sufficient balance
     * When user requests withdraw amount X
     * Then ATM dispenses X, balance reduces by X, and transaction logged

2. **US2 – Kiểm tra số dư (2 SP)**
   *As a customer, I want to check my account balance so that I can know my current financial status.*

3. **US3 – Chuyển khoản (8 SP)**
   *As a customer, I want to transfer money to another account so that I can send payments quickly.*

4. **US4 – Bảo trì (3 SP)**
   *As a technician, I want to maintain the ATM system so that it remains secure and operates reliably.*

---

## Tasks & Phân rã

**US1 – Rút tiền**

* Thiết kế UI/UX: màn hình đăng nhập, chọn số tiền, thông báo kết quả
* Coding: xác thực PIN, kiểm tra số dư, nhả tiền, cập nhật DB
* Testing: PIN đúng/sai, rút thành công, insufficient funds

**US2 – Kiểm tra số dư**

* Thiết kế UI
* Lấy số dư từ DB
* Testing hiển thị số dư

**US3 – Chuyển khoản**

* UI transfer
* API + DB transaction
* Testing (recipient not found, insufficient funds)

**US4 – Bảo trì**

* Chức năng chế độ bảo trì
* Logs & system checks
* Documentation

---

## Sprint Planning

* **Sprint Goal:** Implement withdraw & check balance flows end-to-end.
* **Committed issues:** US1, US2
* **Capacity & Estimates:** ~7 SP committed

---

## Evidence (ảnh chụp)

* Backlog:
  ![Backlog](lab9/backlog.png)

* Sprint Board:
  ![Board](lab9/board.png)

---

