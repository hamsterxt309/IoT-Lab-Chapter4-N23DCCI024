from sense_emu import SenseHat
import time

sense = SenseHat()
r = [255, 0, 0]  # Đỏ
b = [0, 0, 0]    # Tắt

heart = [
    b, b, b, b, b, b, b, b,
    b, r, r, b, r, r, b, b,
    r, r, r, r, r, r, r, b,
    r, r, r, r, r, r, r, b,
    b, r, r, r, r, r, b, b,
    b, b, r, r, r, b, b, b,
    b, b, b, r, b, b, b, b,
    b, b, b, b, b, b, b, b
]
sense.set_pixels(heart)
time.sleep(5)
sense.clear()

