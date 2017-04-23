import random
def dragon_ATK():

    ATK = random.randint(1,45)


    big_dragon_ATK = 130 + ATK


    small_dragon_ATK = 30 + ATK


    very_small_dragon_ATK = 20 + ATK

    n = random.randint(0,2)

    dragon_random = ["big_dragon","small_dragon","very_small_dragon"]
    if n == 0:
        print "big_dragon!!!! ATK:%r"%big_dragon_ATK
        return (dragon_random[n],big_dragon_ATK)
    elif(n == 1):
        print "small_dragon!!!! ATK:%r"%small_dragon_ATK
        return (dragon_random[n],small_dragon_ATK)
    elif(n == 2):
        print "very_small_dragon!!!! ATK:%r"%very_small_dragon_ATK
        return (dragon_random[n],very_small_dragon_ATK)

    else:
        pass
a,b = dragon_ATK()

print "is %r,ATK%r"%(a,b)

for d in range(10):
    print "123"
