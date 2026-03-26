from PIL import Image, ImageStat

# 1. เปิดรูปภาพและแปลงเป็น Grayscale ('L') เพื่อคำนวณค่าความสว่าง
img = Image.open(r"C:\Users\supak\OneDrive\รูปภาพ\Screenshots\Screenshot 2025-12-20 233513.png").convert('L')

# 2. ใช้ ImageStat เพื่อดึงสถิติของรูปภาพ
stat = ImageStat.Stat(img)

# 3. ดึงค่าเฉลี่ยและส่วนเบี่ยงเบนมาตรฐาน (ผลลัพธ์จะเป็น List)
mean_brightness = stat.mean[0]
std_dev = stat.stddev[0]

print(f"ค่าเฉลี่ยแสงสว่าง: {mean_brightness:.2f}")
print(f"ส่วนเบี่ยงเบนมาตรฐาน: {std_dev:.2f}")
img.show()