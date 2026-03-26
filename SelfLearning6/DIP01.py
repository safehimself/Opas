from PIL import Image
im = Image.open("Image1.JPG")
w,h = im.size
#im.show()

for i in range(10,75,1):
    per = i
    dec = 100-per
    newW = int(w*dec/100)
    newH = int(h*dec/100)
    print(w,h)
    print(newW,newH)
    im = im.resize((newW,newH))
    im.save(f"Image1-{i}.JPG")
    #im.show()

