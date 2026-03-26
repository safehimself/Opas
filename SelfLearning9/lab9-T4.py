import re

text = input("กรอกข้อความ: ")

score = 0
keywords = ["ฟรี","ด่วน","คลิก","โปรโมชัน","เงินคืน","รับทันที"]

for word in keywords:
    if word in text:
        score += 2

if re.search(r"http[s]?://", text):
    score += 3

if re.search(r"(.)\1{4,}", text):
    score += 2

print("คะแนน:", score)

if score >= 6:
    print("ระดับ: สแปม")
elif score >= 3:
    print("ระดับ: น่าสงสัย")
else:
    print("ระดับ: ปกติ")
