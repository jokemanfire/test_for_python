from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

def text_char():
    return chr(random.randint(48,122))

def back_color():
    r = random.randint(64,250) # range(0,255)
    g = random.randint(64,250)
    b = random.randint(64,250)
    return (r,g,b)

def text_color():
    r = random.randint(50, 80) # range(0,255)
    g = random.randint(50, 80)
    b = random.randint(50, 80)
    return r,g,b

width = 240
height = 60
img  = Image.new("RGB",(width,height),"white")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('C:\Windows\Fonts\simsunb.ttf', 36)

for h in range(height):
    for w in range(width):
        draw.point((w,h), fill = back_color())

for k in range(4):
    draw.text((60*k + 10, 10),text_char(),font = font ,fill = text_color())

img = img.filter(ImageFilter.BLUR)
img.show()