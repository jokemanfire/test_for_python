from PIL import ImageEnhance
from PIL import Image

sm = Image.open("0.313476033294658.jpg")
enh = ImageEnhance.Contrast(sm)
enh.enhance(0.5).show("70% more contrast")
