from pythainlp.tokenize import word_tokenize
from collections import Counter

def words(text):
    words = word_tokenize(text, engine="newmm")
    
    words = [word for word in words if word.strip()]
    
    word_counts = Counter(words)
    
    top_10 = word_counts.most_common(10)
    
    return top_10


text_example = str(input("กรอกบทความ: "))

result = words(text_example)

print(f"{'อันดับ':<6} | {'คำ':<15} | {'จำนวน':<5}")
print("-" * 30)
for i, (word, count) in enumerate(result, 1):
    print(f"{i:<6} | {word:<15} | {count:<5}")

