import os
import shelve
path = os.path.abspath('.')
print path
file1 = open('/Users/admin/pygitrepository/test.txt',"w")
file1.write("longzitan 15975247846"*5)
file1.close()
file1 = open('/Users/admin/pygitrepository/test.txt',"r")
print file1.read()
print "***"*4
shelfFile = shelve.open("mydata")
cats = ['long','zi','tan']
shelfFile['cats'] = cats
shelfFile.close()
print list(shelfFile.keys())
print list(shelfFile.values())
