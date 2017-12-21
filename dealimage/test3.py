#  encoding:utf-8 
from PIL import Image
import subprocess

def cleanFile(filepath,newfilepath):
    image = Image.open(filepath)
    #对图片进行过滤再保存
    image = image.point(lambda x: 0 if x<143 else 255)
    image.save(newfilepath)
    #调用系统的tesseract命令对图片进行OCR识别
    subprocess.call(["tesseract",newfilepath,"output"])
    #打开文件读取结果
    outputfile = open("output.txt",'r')
    print(outputfile.read())
    outputfile.close()

cleanFile("2.jpg","3.png")
