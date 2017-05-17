spam1 = ['cat','bat','rat','elephant']
print spam1[0]
print spam1[1]
print spam1[int(1.0)]
spam = [['cat','bat'],[10,20,30,40,50]]
print spam[0]
print spam[0][1]
print spam[1][4]
print spam1[-1]
print spam1[-3]
print spam[1][-2]
print spam1[0:3]
print spam1[1:3]
print spam1[0:-1]
print spam[:]
print len(spam)
spam1[1] = "aardvark"
spam[1][-1] = "1234"
print spam1
print spam[1]
del spam1[2]
print spam1
catNames = []
while True:
    print ("Enter the name of cat"+ str(len(catNames)+1)+('Or enter nothing to stop'))
    name = raw_input()
    if name == "":
        break
    catNames = catNames + [name]
print "the cat name are:"
for name in catNames:
    print (''+name)
print catNames
for i in range(4):
    print i
supplies = ['pens','staplers','flame-thrower','binders']
for i in range(len(supplies)):
    print ('index'+str(i)+ "in supplies is:" + supplies[i])
print ("*"*20+"next is (in ,not in)")
print supplies.index('pens')
print ("*"*20 + "next are append insert")
spam2 = ['hello','kitty','boy','girl']
spam2.append('little')
spam2.append(['boy','maby','your'])
spam2.insert([5][0],'GAME')
spam2.insert([6][0],"sunshine")
print spam2
for list in spam2:
    print list
for x in spam2[7]:
    print x
spam2.remove("hello")
print spam2
spam_sort = [0,12,47,2.2]
spam_sort.sort()
print spam_sort
spam_sort.sort(reverse=True)
print spam_sort
spam_sort_str = ['long','Z','T','A','a']
spam_sort_str.sort(key=str.lower)
print spam_sort_str
print "****"*20
name_string = 'zophie is cat'
new_string = name_string[0:7] + 'the' + name_string[8:]
print new_string
print "----"*5
list_1 = [0,12,35,6]
tuple_1 = ('5','4','3')
print tuple(list_1)
print list('long')
