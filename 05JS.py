tom = ['a','x','f','d','m']
tom1 = ['2','4','7','1']
tom.extend([1,23,5])
print tom
tom2 = [tom,tom1]
print tom2
tom1.insert(2,"z")
print tom1
tom1.append("one")
print tom1

tom.pop()
tom.remove("a")
print tom
