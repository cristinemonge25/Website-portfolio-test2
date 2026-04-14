import os
from PIL import Image

for name in ['galerie2.png', 'galerie3.png', 'galerie4.png', 'galerie5.png', 'galerie6.png']:
    try:
        path = os.path.join('images', name)
        img = Image.open(path).convert('L')
        crop = img.crop((50, 50, 400, 200))
        dark_pixels = sum(1 for p in crop.getdata() if p < 240)
        print(f"{name}: {dark_pixels} dark pixels in top left")
    except Exception as e:
        print(f"{name}: error {e}")
