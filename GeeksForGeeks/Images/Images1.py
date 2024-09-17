import
import ImageFilter
img = Image.open('/Users/veerapulapakura/downloads/squirtle.jpg')
print(img)
print(img.format)
print(img.size)
print(img.mode)

filterdimage = img.filter(ImageFilter.BLUR)
filterdimage.save('blur.png','png')
# /Users/veerapulapakura/PycharmProjects/PythonDevLearning/venv/Images
filterdimage = img.filter(ImageFilter.SMOOTH)

filterdimage.save('SMMOTH.png','png')

filterdimage = img.convert('L')
rotated_image = filterdimage.rotate(90)
rotated_image.save('grey.png','png')


resize_image = filterdimage.resize((300,300))
resize_image.save('re.png','png')

box = (100,100,300,300)
croped = filterdimage.crop(box)
croped.save('cropped.png','png')