#coding:utf-8
import re
keys2 = re.compile(r"(\d\d\d-\d\d\d)")
keys3 = re.compile(r"(\w)*(\s){1}(\D)*")
keys4 = re.compile(r'^\d\d\d$')
keys5 = re.compile(r'.at')
m3 = keys2.findall("hahaha 123-321 123-456 123-789")
m4 = keys4.findall("w533")
m5 = keys5.findall("lat zitat xiat duat")
print "__"*3
keys6 = re.compile(r'long:(.*)zi:(.*)')
m6 = keys6.search("long:zitan zi:nihao fsdlfjasfadsfjlsadfjas")
print m6.group()
keys7 = re.compile(r'Agent \w+ \w+')
x = keys7.sub('subreplace','Agent long zitankljflsdajfalsjd dfass')
print x
email = re.compile(r'([0-9a-zA-Z]+@[0-9a-zA-Z]+\.[a-zA-Z]{2,4})')
x1 = email.findall("longzitan@126.com")
print x1
print "--"*5
txtmatch = re.compile(r'([0-9]+)')
print txtmatch.findall("ruby python 15974247846 long")

f = open('/Users/admin/pygitrepository/test.txt','r')
txtnumber = txtmatch.findall(f.read())
print txtnumber
print "***"*5

passwd = re.compile(r'([0-9]{1,2}[0-9]{0,3}[0-9]{0,3})')
door = passwd.findall("12")
door1 = passwd.findall("12,134,666")
print door
print door1
name = re.compile(r'([a-zA-Z]*\.)\s([a-zA-Z]*)',re.I)
print name.findall("Mr. long ZI TAN ")
