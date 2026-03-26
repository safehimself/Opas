from PIL import Image
img = Image.open('Image1.jpg')
w, h = img.size
new_img = img.resize((w*2,h*2))
new_img.save("New_Image.jpg")
print("Old Image Size:", img.size)
print("New Image Size:", new_img.size)
