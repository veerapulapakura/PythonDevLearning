import PIL
from PIL import Image, ImageFilter
img = Image.open('/Users/veerapulapakura/downloads/charmander.jpg')
print(img)
print(img.size)

# resized = img.resize((100,100))
# print(resized)
# resized.save('newimaze.png', 'png')
img.thumbnail((100,100))
img.save('thumbnail.png')
