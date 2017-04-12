import re
line = "cats are smarter than dogs"
matchobj =  re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchobj:
    print "matchobj.group():",matchobj.group()
else:
    print "no match"
