import re
mo = re.compile(r'b\w?t')
abc = mo.findall('bat bit but hat hit hut')
print abc
mo1 = re.compile(r'\w*\s\w*')
abc1 = mo1.findall('hi! how are you today?')
print abc1
abc2 = "Smith Far"
mo2 = re.split(r',',"Smith")
print mo2
mo3 = re.compile(r'\d*\w.*')
abc3 = mo3.findall("2014 changsha Drive 35-5")
print abc3
mo4 = re.compile(r'(www.\w*|\d*.com|.edu|.org)')
abc4 = mo4.findall("www.baidu.com www.126.edu")
print abc4
mo5 = re.compile(r"^\d*$")
abc5 = mo5.search("12415")
print abc5.group(0)
