from PIL import Image, ImageDraw

def clean(filename, out):
    img = Image.open(filename).convert('RGB')
    draw = ImageDraw.Draw(img)
    w, h = img.size
    print(f"Size of {filename}: {w}x{h}")
    # Cover top left
    draw.rectangle([0, 0, w*0.4, h*0.3], fill=(255, 255, 255))
    
    # Cover bottom left (Perspective 1)
    # the background is greyish at the bottom. We can copy a patch from the right side of the bottom.
    patch_w = int(w * 0.2)
    patch_h = int(h * 0.1)
    y_start = h - patch_h
    # patch from x=w//2
    patch = img.crop((w//2, y_start, w//2 + patch_w, h))
    img.paste(patch, (0, y_start))
    
    img.save(out)
    print(f"Saved to {out}")

clean('images/harbor-new-1.png', 'images/harbor-new-1-clean.png')
# Also clean hero-home-new.png if it has the text
clean('images/hero-home-new.png', 'images/hero-home-new-clean.png')
