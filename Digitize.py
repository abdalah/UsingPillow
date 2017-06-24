# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 16:11:12 2017

@author: abdalah
"""

from PIL import Image, ImageDraw, ImageFont

# Load Image
picture = Image.open("example.jpg")
width, height = picture.size

# Create Empty Image
txt = Image.new("RGBA", picture.size, (255,255,255))
# get a drawing context
d = ImageDraw.Draw(txt)

# Load Font
fnt = ImageFont.truetype('Times New Roman.ttf', size=8)

# Get Digits of Pi
f = open("Pi.txt", 'r')
pi = f.readline()

i=0
# Process every 8 pixels put a digit
for y in range(0, height, 8):
    for x in range(0, width, 4):
        d.text((x,y), pi[i], font=fnt, fill=picture.getpixel( (x,y) ))
        i+=1

txt.show()
txt.save("digitizedExample.png")