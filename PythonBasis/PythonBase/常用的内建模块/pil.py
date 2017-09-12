
from PIL import Image,ImageFilter,ImageFont,ImageDraw
import random

def imageMOHU():
    im = Image.open('1.jpg')
    im2 = im.filter(ImageFilter.BLUR)
    im2.save('blur.jpg', 'jpeg')


#随机字母
def rndChar():
        return '单雪梅'#chr(random.randint(65,90))
#随机颜色
def rndColor():
         return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
#随机颜色二
def rndColor2():
         return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width = 80*4
height = 100
image = Image.new('RGB',(width,height),(255,255,255))
font = ImageFont.truetype('Arial.ttf',36)
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill = rndColor() )

for t in range(5):
    draw.text((80*t+10,10),"xuemei",font=font,fill=rndColor2())

image = image.filter(ImageFilter.BLUR)
image.save('xs.jpg','jpeg')