import os
from collections import defaultdict, Counter
from pythainlp.tokenize import word_tokenize

folder_path = "Documents"

inverted_index = defaultdict(dict)

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        with open(os.path.join(folder_path, filename), "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
            tokens = word_tokenize(text.lower())
            count = Counter(tokens)

            for word, freq in count.items():
                inverted_index[word][filename] = freq

query = input("ค้นหา: ").lower()

if query in inverted_index:
    results = inverted_index[query]
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    print("ผลการค้นหา:")
    for file, freq in sorted_results:
        print(f"{file} (พบ {freq} ครั้ง)")
else:
    print("ไม่พบคำนี้ในเอกสาร")

