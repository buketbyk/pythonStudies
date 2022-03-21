from PIL import Image,ImageFilter
''' you need to have the same images in your project folder.'''
image = Image.open("kuş.jpg")

image.save("kuş2.jpg")

image.rotate(180).save("kuş3.jpg")


image.rotate(90).save("kuş4.jpg")

image.convert(mode = "L").save("kuş5.jpg")

degistir = (960,600)

image.thumbnail(degistir)

image.save("kuş6.jpg")

image.filter(ImageFilter.GaussianBlur(10)).save("kuş8.jpg")

kırpılacak_alan = (340,0,950,600)

image2 = Image.open("atatürk.jpg")
image2.crop(kırpılacak_alan).save("kuş9.jpg")
