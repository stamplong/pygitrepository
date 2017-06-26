import E48
df = E48.lexicon()
word_list = df.scan('longzitan 123 up down 456 789 10000')

word_list_1 = sorted(word_list,reverse=True)
sentence = ' '
for i in range(0,len(word_list_1)):
    for x in word_list[i]:

        if x =='verb':
            ST = word_list_1[i][1]
            sentence = ST + " " + sentence

        elif x =='direction':
            ST_1 = str(word_list_1[i][1])
            sentence = ST_1 + " "+sentence

        elif x =='number':
            ST_2 = str(word_list_1[i][1])
            sentence = ST_2 +" " + sentence

        elif x =='error':
            continue
print sentence
