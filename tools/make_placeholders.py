# Regenerates grey placeholder covers. Usage: python3 tools/make_placeholders.py  (needs Pillow)
from PIL import Image, ImageDraw, ImageFont
T=[("Northwind Banking App","L"),("Lumen Design System","L"),("Atlas Travel Platform","L"),("Verde Brand & Web","L"),("Portrait (About)","P")]
F="/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf"
def font(s,b=False):
    try: return ImageFont.truetype(F%("-Bold" if b else ""),s)
    except OSError: return ImageFont.load_default()
for i,(t,o) in enumerate(T,1):
    w,h=(1920,1080) if o=="L" else (1080,1920)
    im=Image.new("RGB",(w,h)); d=ImageDraw.Draw(im)
    for y in range(h):  # soft neutral vertical gradient
        v=int(232-18*y/h); d.line([(0,y),(w,y)],fill=(v,v,v+2))
    m=int(min(w,h)*.06); d.rectangle([m,m,w-m,h-m],outline=(188,189,192),width=3)
    def c(txt,f,y,col):
        b=d.textbbox((0,0),txt,font=f); d.text(((w-(b[2]-b[0]))/2,y),txt,font=f,fill=col)
    c("COVER IMAGE",font(int(min(w,h)*.032)),h*.40,(130,132,138))
    c(t,font(int(min(w,h)*.062),True),h*.47,(58,60,66))
    c(f"{w} × {h}",font(int(min(w,h)*.028)),h*.58,(140,142,148))
    im.save(f"assets/projects/project-{i:02d}.webp",quality=88)
