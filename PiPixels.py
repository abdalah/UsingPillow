# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 23:43:36 2017

@author: abdalah
"""

from PIL import Image, ImageDraw, ImageFont
# Import Image
picture = Image.open("example.jpg")
width, height = picture.size

# Create New Image
txt = Image.new("RGBA", picture.size, (255,255,255))
# get a drawing context
d = ImageDraw.Draw(txt)

# Load Font
fnt = ImageFont.truetype('Times New Roman.ttf', size=18)

# For Every 9 Pixels Put π
for x in range(0, width, 9):
    for y in range(0, height, 9):
        d.text((x,y), "π", font=fnt, fill=picture.getpixel( (x,y) ))

txt.show()
txt.save("piExample.png")