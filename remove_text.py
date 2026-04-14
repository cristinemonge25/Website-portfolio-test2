from PIL import Image, ImageDraw

img = Image.open('images/galerie1.png').convert('RGB')
draw = ImageDraw.Draw(img)

# Cover top left text (Sector Plaza...) with white. The background is plain white there.
draw.rectangle([0, 0, 700, 400], fill=(255, 255, 255))

# Cover bottom left text (Perspective 1) with a textured patch from just to the right of it.
patch = img.crop((300, 950, 600, 1080))
img.paste(patch, (0, 950))
# Let's paste again just to cover more to the right if needed
patch2 = img.crop((600, 950, 900, 1080))
img.paste(patch2, (200, 950))

img.save('images/hero-bg.png')
print("Image processed and saved to images/hero-bg.png")
