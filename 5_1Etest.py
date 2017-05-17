stuff = {'rope':1,'torch':2,'gold coin':43,'darger':4}
def displayInventory(stuff):
    total = 0
    for x,v in stuff.items():
        print x,
        print v
        print '\n'
displayInventory(stuff)
