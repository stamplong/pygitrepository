import re
line = "cats are smarter than dogs"
matchobj =  re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchobj:
    print "matchobj.group():",matchobj.group()
else:
    print "no match"
dic = {'longz':"123",'zi':"4n56"}
for i in dic:
    print "dic[%s]"%i,dic[i]
for (k,v)in dic.items():
    print "dic[%s]"%k,v

print dic.keys()
print dic.items()
print dic.values()
print dic.get("longzitan")
print dic.get("longz")
print dic
print dic.update({"123":"456"})
print dic
print dic.setdefault("123","789")
print dic.setdefault("333","444")
print dic
print dic.pop("longz")
print dic
