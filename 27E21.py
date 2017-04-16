def add(a,b):
    print "adding %d + %d"%(a,b)
    return a +b
def subtract(a,b):
    print "subtracting %d - %d"%(a,b)
    return a - b
def multiply(a,b):
    print "multiplaying %d * %d"%(a,b)
    return a * b
def divide(a,b):
    print "dividing %d / %d"%(a,b)
    return a/b

print "let's some math with just functions"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age:  %d,Height:  %d Weight: %d, IQ: %d"%(age,height,weight,iq)

print "here is a puzzle"

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print "That becomes:",what,"Can you do ti by hand?"
