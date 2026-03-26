from datetime import datetime
from gtts import gTTS

name = input("ชื่อ: ")
now = datetime.now()

days = ["วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี",
        "วันศุกร์", "วันเสาร์", "วันอาทิตย์"]
months = ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม",
          "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน",
          "ตุลาคม", "พฤศจิกายน", "ธันวาคม"]

message = (
    f"สวัสดีคุณ{name} "
    f"วันนี้{days[now.weekday()]}{now.day} {months[now.month-1]} "
    f"ปีพุทธศักราช {now.year + 543} "
    f"ขณะนี้เวลา {now.hour} นาฬิกา {now.minute} นาที "
    f"วันนี้เป็นวันครบรอบวันเกิดของคุณ ขอให้คุณมีความสุขมากมากนะคะ"
)

print(message)

gTTS(message, lang="th").save("birthday.mp3")
