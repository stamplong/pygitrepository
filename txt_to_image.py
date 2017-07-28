from PIL import Image,ImageDraw,ImageFont
import os

a = {'go':'','hospital':'','changsha':''}
src = os.getcwd()
src_1 = src + "/txttoimage.txt"


search = open(src_1,'r')

search_read = search.read()

search_string = search_read.split()
d = []

for i in range(0,len(search_string)):
    c = search_string[i]
    if c in a:
        d.append(c)
print d

im = Image.new('RGBA',(200,200),'white')
draw = ImageDraw.Draw(im)
myfont = ImageFont.truetype('YuMincho.ttc',size=80)
fillcolor = 'pink'

draw.text((100,100),d[0],font=myfont,fill=fillcolor)
im.save('image_11.png')
