from PIL import ImageDraw,ImageFont,Image

a = {'long':'','tan':'','zi':''}
b = ['zi','tan','t']
f = []
for x in range(0,len(b)):
    if b[x] in a:
        f.append(b[x])
print f
for x in b:
    if len(x)==3:
        for f in x:
            print f

im = Image.new('RGBA',(800,800),'white')
image = ImageDraw.Draw(im)
myfont = ImageFont.truetype('YuMincho.ttc',size=40)
fillcolor = 'pink'
