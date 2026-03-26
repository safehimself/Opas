from PIL import Image
im = Image.open("TestPicture.jpg")
w,h = im.size

for i in range(w):
    for j in range(h):
        r,g,b = im.getpixel((i,j))
        Max = max(r, g, b)
        im.putpixel((i,j),(Max,Max,Max))
im.show()
#im.save("result1.jpg")


im = Image.open("TestPicture.jpg")
for i in range(w):
    for j in range(h):
        r,g,b = im.getpixel((i,j))
        nr = int(0.393*r + 0.769*g + 0.189*b)
        ng = int(0.349*r + 0.686*g + 0.168*b)
        nb = int(0.272*r + 0.534*g + 0.131*b)

        if nr > 255 : nr = 255
        else : nr = nr
        if ng > 255 : ng = 255
        else : ng = ng
        if nb > 255 : nb = 255
        else : nb = nb
        im.putpixel((i, j), (nr, ng, nb))
im.show()
#im.save("result2.jpg")

im = Image.open("TestPicture.jpg")
from PIL import Image, ImageOps
im_gray = ImageOps.grayscale(im)
im_gray = ImageOps.autocontrast(im_gray)
black_color = "#002060"
white_color = "#e0ffff"
cyanotype = ImageOps.colorize(im_gray, black=black_color, white=white_color)
cyanotype.show()
cyanotype.save("result3.jpg")
