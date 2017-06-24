from PIL import Image

# Get new Image ready
newImg = Image.new('RGB', (1152, 1090-400))

# Length of Each Image Divided By 4
lengths = 1152/4
# Create Each Image and add it to the photo
for i in range(4):
    img1 = Image.open("pic%i.png" % i)
    img = img1.crop((lengths*i, 400, lengths*(i+1), 1090))
    newImg.paste(img, (int(lengths)*i, 0))
newImg.show()
newImg.save('final.png')