from PIL import Image

image = Image.open("monro.jpg")
channels = image.split()
red, green, blue = channels

width = image.width
height = image.height
img_size = (width-50, height)
alpha = 0.3

red_left = red.transform(img_size, Image.EXTENT, (50, 0, width, height))
red_rigth = red.transform(img_size, Image.EXTENT, (25, 0, width-25, height))
img_blend_red = Image.blend(red_left, red_rigth, alpha)

blue_left = blue.transform(img_size, Image.EXTENT, (25, 0, width-25, height))
blue_right = blue.transform(img_size, Image.EXTENT, (0, 0, width-50, height))
img_blend_blue = Image.blend(blue_right, blue_left, alpha)

img_green = green.transform(img_size, Image.EXTENT, (25, 0, width-25, height))

new_image = Image.merge("RGB", (img_blend_red, img_green, img_blend_blue))
new_image.thumbnail((80, 80))
new_image.save('monro.jpg')
