def fun1():
    for i in range(1,5):
        return i
def fun2():
    for i in range(1,5):
        print i
def fun3():
    for i in range(1,5):
        yield i


print fun1()
print "--------------\n"
print fun2()
print "--------------\n"
print "yield function"
x = []
x = fun3()
for i in x:
    print i,"xxx:::"
