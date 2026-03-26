import re

text = input("กรอกข้อความ: ")
print("Before:", text)

text = re.sub(r"\s+", " ", text)

text = text.lower()

text = re.sub(r"[^\w\sก-๙]", "", text)

print("After:", text)
