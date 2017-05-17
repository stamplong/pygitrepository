import pprint
dic_1 = {'a':1,'egg':2,'apples':3}
print dic_1.get('egg',0)
print dic_1.setdefault('apples',4)
print dic_1.setdefault('color','white')

print "*"*20
string_1 = "longianndlsfjasl faksdjfsdaf  asdfj"
count = {}
for character in string_1:
    count.setdefault(character,0)
    count[character] = count[character] + 1
print count
print "*"*20

pprint.pprint(count)
print (pprint.pformat(count))
foods = {'Alice':{'apple':5,'dog':3},
        'jason':{'apple':2,'dog':2}}
