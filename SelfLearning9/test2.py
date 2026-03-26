import requests
from bs4 import BeautifulSoup

url = 'https://www.sc.su.ac.th'

try:
    # 1. ดึงข้อมูลจากเว็บไซต์
    response = requests.get(url)
    response.encoding = 'utf-8' # กำหนด Encoding เป็น utf-8 สำหรับภาษาไทย
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 2. ค้นหาข้อมูล (ในที่นี้ขอดึงหัวข้อจาก Tag h1-h3 เป็นตัวอย่าง)
        # คุณสามารถเปลี่ยน 'h3' เป็น class ที่ต้องการได้ เช่น soup.find_all('div', class_='news-title')
        items = soup.find_all(['h1', 'h2', 'h3'])
        
        # 3. บันทึกผลลงไฟล์ result.txt
        with open('result.txt', 'w', encoding='utf-8') as f:
            for index, item in enumerate(items, 1):
                text_data = item.get_text(strip=True)
                if text_data: # บันทึกเฉพาะบรรทัดที่มีข้อความ
                    line = f"{index}. {text_data}\n"
                    f.write(line)
                    print(f"Saved: {line.strip()}")
        
        print("-" * 30)
        print("บันทึกข้อมูลลงใน result.txt เรียบร้อยแล้วครับ!")
        
    else:
        print(f"ไม่สามารถดึงข้อมูลได้ (Error Code: {response.status_code})")

except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")
