dragonloot = ['gold coin','darger','rope','gold coin','rope']
inventory = {}
def displayinventory(inventory,dragonloot):
    a = {}
    for x in dragonloot:
        a.setdefault(x,0)
        a[x]+=1
    for y in inventory:
        if y not in a:
            a.setdefault(y,0)
            a[y] += inventory[y]
    print a
displayinventory(inventory,dragonloot)
