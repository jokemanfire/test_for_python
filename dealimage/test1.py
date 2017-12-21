from PIL import Image,ImageFilter

kitten = Image.open("0.313476033294658.jpg")
blurrykitten = kitten.filter(ImageFilter.GaussianBlur)
blurrykitten.save("1.jpg")
blurrykitten.show()