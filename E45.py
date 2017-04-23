import random

human_bag = {'rope':1,'goldcoin':47,'dagger':1,'arrow':1}
ATK1 = human_bag.get("rope") + human_bag.get("dagger") + human_bag.get("arrow")
global human_ATK
global goldcoin
global Red
Red = 500
human_ATK = ATK1 + 100
goldcoin = 100

print "between human and dragon fight"
print "human of ATK"
name = raw_input("please enter your name My hero**** >>>")
print "%r_ATK::%rMy DPS....."%(name,human_ATK)
drop_out = ["rope","goldcoin","dagger","arrow"]
print "My bag have:"
for i in human_bag.keys():
    print(i)
print "I am a brave people,i must win this war for all of human"
print "*****finding****"


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


def dragon_die():
    drop_out_one = random.randint(0,4)
    rope_1 = random.randint(0,10)
    goldcoin_1 = random.randint(0,48)
    dagger_1 = random.randint(0,10)
    arrow_1 = random.randint(0,12)
    dead_drop_out = drop_out[drop_out_one]
    if drop_out_one == 0:
        print "OH!!!My god drop out rope!!!"
        print "Human ATK++++%r"%(rope_1+human_ATK)
    elif(drop_out_one==1):
        print "OH!!!My god drop out goldcoin,i'm rich"
        print "Human goldcoin++++%r"%(goldcoin+goldcoin_1)
    elif(drop_out_one == 2):
        print "OH!!!My god drop out dagger!!!"
        print "ATK++++%r"%(human_ATK+dagger_1)
    elif(drop_out_one == 3):
        print "OH!!!My god drop out arrow!!!"
        print "ATK++++%r"%(human_ATK+arrow_1)
    else:
        print"nothing in dragon"


def win():
    for d in range(5):
        dragonnew,dragon_ATK11 = dragon_ATK()

        print "it is a %s,ATK=:%r"%(dragonnew,dragon_ATK11)

        win_ATK = human_ATK - dragon_ATK11
        Red1 = Red - int(win_ATK)*0.3

        if(win_ATK >=0):
            print "human win"
            dragon_die()
            print "******"*30
            print "human Red:",Red1
            print "win goldcoin",goldcoin
            print "human_ATK:",win_ATK
            print "******"*30
        else:
            print "need ATK_medicine and more red"
            Red1 = int(raw_input("need more Red_medicine>>>"))
            win_ATK = int(raw_input("need more ATK_medicine>>>"))
            print "life restart``````"
win()
