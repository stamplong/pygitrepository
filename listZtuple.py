import copy
list_1 = ['a','b','c']
tuple_1 = ('l','o','n','g')
print list(tuple_1)
print tuple(list_1)
print ''.join(list_1)
spam = 42
chesse = spam
spam = 100
print spam
print chesse
print "**"*20
list_z = list(tuple_1)
print list_z
list_2 = list_z.append('hellofile')
print list_2
print "**"*20
spam = ['2','4']
chesse_1 = copy.copy(spam)
print chesse_1
print int('3'*2)
