from PIL import Image, ImageChops
image_path = ("rotated.jpg")
def trim(image_path):
    im = Image.open(image_path)
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
crop_image = trim(image_path)
crop_image.show()