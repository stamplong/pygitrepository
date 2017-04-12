#! usr/bin/python
#coding=utf-8
list1 = [3,2,5,6,7,4]
list2 = list1
list2.sort(reverse = True)
print list1
print list2
new = list2[:]
new.sort()
print new
print list2
new1 = sorted(list1)
a = 123
print("new list %s %f"%(new1,1.83))

print list1
print("舒克L")
