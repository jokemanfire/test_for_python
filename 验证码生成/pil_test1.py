from PIL import Image, ImageFilter
import time


im = Image.open("test.jpg")
img = Image.open('1.jpg')
im1 = im.filter(ImageFilter.BLUR) #模糊滤波


im2 = im.filter(ImageFilter.CONTOUR) #轮廓滤波

im3 = img.filter(ImageFilter.DETAIL) #细节增强滤波

#im2 = im2.filter(ImageFilter.EDGE_ENHANCE) #边缘增强

im4 = img.filter(ImageFilter.EDGE_ENHANCE_MORE) #边缘超级增强

im5 = im.filter(ImageFilter.EMBOSS) #浮雕效果

im6 = im.filter(ImageFilter.FIND_EDGES) #寻找边缘信息

im6.show()