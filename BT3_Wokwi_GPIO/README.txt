# BÀI TẬP 3 — GPIO & SENSOR (WOKWI)

## Nền tảng
- Raspberry Pi Pico
- MicroPython
- Wokwi Simulator

---

## 1. Đèn giao thông (Traffic Light)
- 3 LED: đỏ (GP15), vàng (GP14), xanh (GP13)
- Chu kỳ:
  - Đỏ: 5s
  - Xanh: 5s
  - Vàng: 2s

🔗 Link Wokwi:
https://wokwi.com/projects/462002681953108993

---

## 2. DHT22 — Đọc nhiệt độ & độ ẩm
- Sensor: DHT22
- Chân DATA: GP16
- Đọc dữ liệu mỗi 2 giây

🔗 Link Wokwi:
https://wokwi.com/projects/462002794294437889

---

## 3. Cảnh báo nhiệt độ/độ ẩm bằng LED
- Temp > 30°C → LED đỏ
- Humidity > 80% → LED vàng
- Bình thường → LED xanh

🔗 Link Wokwi:
https://wokwi.com/projects/462002865683607553

---

## 4. ADC + Potentiometer
- Đọc giá trị từ GP26
- Chia 3 mức:
  - <33% → THẤP (LED xanh)
  - 33–66% → TRUNG BÌNH (LED xanh + vàng)
  - >66% → CAO (3 LED)

🔗 Link Wokwi:
https://wokwi.com/projects/461969987391031297

---

## Demo
- Có thể thay đổi nhiệt độ/độ ẩm bằng slider trên Wokwi
- Xoay potentiometer để thay đổi mức LED

---

## Ảnh minh chứng
Xem trong thư mục:
../screenshots/