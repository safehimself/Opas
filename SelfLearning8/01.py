from pythainlp.tokenize import subword_tokenize
name = input("ชื่อ : ")
syllables = subword_tokenize(name)
groups = {
    1: "กถทภดะาำุ่ฤๅ",
    2: "ขชงบปเแู้",
    3: "ตฆฑฒ๋",
    4: "คธญรษโิะั",
    5: "ฉฌณนมหฎฮฬึ",
    6: "จลวอใ",
    7: "ซศสีื๊",
    8: "ยผฝพฟ็",
    9: "ฎฏฐ์ไ"
}
score_map = {}
for score, chars in groups.items():  
    for char in chars:               
        score_map[char] = score
total_score = 0
for syl in syllables:
    for char in list(syl):
        point = score_map.get(char, 0)
        total_score += point
        if point > 0:
            print(f"{char} = {point}")
print(f"รวมคะแนนเลขศาสตร์ได้: {total_score}")
very_good_list = [2, 4, 5, 6, 9, 14, 15, 19, 23, 24, 36, 41, 42, 45, 46, 50, 51, 53, 55, 56, 59, 63, 64, 65]
good_list = [20, 32, 40, 44, 69, 79]
bad_list = [27, 29, 30]
if total_score in very_good_list:
    result = "ดีมาก (Very Good)"
elif total_score in good_list:
    result = "ดี (Good)"
elif total_score in bad_list:
    result = "ให้โทษ (Harmful)"
else:
    result = "ไม่ระบุบในกลุ่มใด"
print(f"วิเคราะห์ตามหลักนามศาสตร์: {result}")
