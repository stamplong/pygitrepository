#-*- coding:utf-8 -*-
import pylab

from wordcloud import WordCloud
font = "/Library/Fonts/华文细黑.ttf"
import matplotlib.pyplot as plt
filename = 'txttoimage.txt'
with open(filename) as f:
    mytext = f.read()
    print(mytext)

wordcloud = WordCloud(font_path=font).generate(mytext)
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.show()
