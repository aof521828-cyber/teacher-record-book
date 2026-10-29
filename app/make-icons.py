"""Generate launcher icons and splash screens from the college seal (assets-logo.png)."""
import os
from PIL import Image, ImageDraw
R = 'android/app/src/main/res'
logo = Image.open('assets-logo.png').convert('RGBA')
def fit(img, size):
    return img.resize((size, size), Image.LANCZOS)
dens = {'mdpi': 1, 'hdpi': 1.5, 'xhdpi': 2, 'xxhdpi': 3, 'xxxhdpi': 4}
for d, k in dens.items():
    os.makedirs(f'{R}/mipmap-{d}', exist_ok=True)
    s = int(48 * k)
    # legacy square + round icons: white disc with the seal
    for name in ('ic_launcher', 'ic_launcher_round'):
        im = Image.new('RGBA', (s, s), (0, 0, 0, 0))
        ImageDraw.Draw(im).ellipse((0, 0, s - 1, s - 1), fill='white')
        L = fit(logo, int(s * 0.9)); im.alpha_composite(L, ((s - L.width) // 2, (s - L.height) // 2))
        im.save(f'{R}/mipmap-{d}/{name}.png')
    # adaptive foreground (108dp canvas, seal inside the 66dp safe zone)
    f = int(108 * k); im = Image.new('RGBA', (f, f), (0, 0, 0, 0))
    L = fit(logo, int(f * 0.62)); im.alpha_composite(L, ((f - L.width) // 2, (f - L.height) // 2))
    im.save(f'{R}/mipmap-{d}/ic_launcher_foreground.png')
# splash screens: white with the seal and app name area left clean
for folder in os.listdir(R):
    p = f'{R}/{folder}/splash.png'
    if os.path.exists(p):
        w, h = Image.open(p).size
        im = Image.new('RGBA', (w, h), 'white')
        L = fit(logo, int(min(w, h) * 0.32)); im.alpha_composite(L, ((w - L.width) // 2, (h - L.height) // 2))
        im.convert('RGB').save(p)
# drop the template's vector foreground so the seal is used everywhere
v = f'{R}/drawable-v24/ic_launcher_foreground.xml'
if os.path.exists(v): os.remove(v)
print('icons ok')
