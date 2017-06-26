import re
abc = re.compile(r'[a-zA-Z]*\d*-\d*-\d*::\w*')

mo1 = abc.findall("Thu 2017-11-30::username")
print mo1

abc1 = re.compile(r'man(fire)?|(zitan)')
mo2 = abc1.findall("manfirezitan")
print mo2
abc2 = re.compile(r'(first Name:)(.*)([1-9a-zA-Z]*)')
mo3 = abc2.findall("first Name: dfasdfljdaslfjdsfl 123467")
print mo3
x = list(mo3[0])
print x
print ','.join(x)
mt = "long 123-456"
x = re.sub('long',"hello world!",mt)
print x
