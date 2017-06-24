# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 10:41:55 2017

@author: abdalah
"""
from PIL import Image, ImageDraw, ImageFont
# Load Image
picture = Image.open("example.jpg")
width, height = picture.size

# Create a New Image With Size "size"
size = min(width, height)
txt = Image.new("RGBA", (size, size), (255,255,255))
# get a drawing context
d = ImageDraw.Draw(txt)


# Load Font
fnt = ImageFont.truetype('Times New Roman.ttf', size=size*2)

# Draw Large π
d.text((0,-7*size/8), "π", font=fnt, fill=(0,0,0))


img = Image.new('RGB', (size, size), "black")
pixels = img.load()
ch=20
# Process every pixel
for x in range(size):
    for y in range(size):
        # If it's black, draw it darker
        if txt.getpixel((x,y)) != (255, 255, 255, 255):
            t = picture.getpixel( (x,y) )
            t = [i-ch for i in t]
            t = tuple(t)
            pixels[x,y] = t
        else:
            pixels[x,y] = picture.getpixel( (x,y) )

img.show()
img.save("shaderExapmle.png")