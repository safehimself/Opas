from PIL import Image
import numpy as np
img = Image.open('Image1.jpg')
w,h = img.size
for i in range(w):
    for j in range(h):
        r,g,b = img.getpixel((i,j))
        c = (r+g+b)//3
        img.putpixel((i,j),(c,c,c))
img.save("Grayscale.jpg")
Color = np.array(img)
print("Mean_Color:", Color.mean())
print("Std_Color:", Color.std())
