import qrcode
data = "https://leetcode.com/"
img = qrcode.make(data)
img.save("my_qr_code1.png")
img.show()