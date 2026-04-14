from PIL import Image, ImageDraw

img = Image.open('images/hero-home.png').convert('RGB')
draw = ImageDraw.Draw(img)

draw.rectangle([0, 0, 1000, 600], fill=(255, 255, 255))

patch = img.crop((800, 1300, 1400, 1444))
img.paste(patch, (0, 1300))

patch2 = img.crop((1400, 1300, 2000, 1444))
img.paste(patch2, (500, 1300))

img.save('images/hero-home.png')
print("Image processed successfully")
