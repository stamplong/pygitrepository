student1 = [1,2,3,4]
student2 = [34,46,27,80]
student3 = [13,45,29,90]

classmarks = [student1,student2,student3]
new1 = classmarks[:]
del classmarks[1][2]

print classmarks
print new1

y = student3.pop()
print y
print student3
x = []
x.extend(["123","456"])
print x
