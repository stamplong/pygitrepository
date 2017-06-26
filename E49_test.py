import E48
df = E48.lexicon()
word_list = df.scan('long zi tan up right 123')
print word_list
word_list_1 = 'long zi tna 123 5 66'
list_1 = word_list_1.split()
print list_1
sentence = ''
list_2 = sorted(list_1,reverse=True)
print list_2
for i in list_2:
    sentence = i + ' ' + sentence
print sentence
