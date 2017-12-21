from PIL import Image

im = Image.open("test.jpg")
out = im.point(lambda i:i*1.2+10)
out.show()
#r,g,b = im.split()
#im = Image.merge("RGB",(b,g,r)) #通道交换
#im.show()
#im.close()