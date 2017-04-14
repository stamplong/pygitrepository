from sys import argv
from os.path import exists

script,first,second = argv

abc = open(argv[1],"a+")
cba = open(argv[2],"a+")

xx1 = abc.read()
xx2 = cba.read()

print "first abc%r\n how long::::%r"%(xx1,len(xx1))
print "\n"
print "\n"
print "\n"
print "second cba%r\n how long::::%r"%(xx2,len(xx2))
print "\n"
print "\n"

xx1.write(xx2,"\n")#help me modification
print xxx1
xx1.close()
xx2.close()
