class Gameobject:
    def long2(self,name):
        self.name = name
        return name
    def pickup(self,player):
        self.player = player
        return self.player + self.name

a = Gameobject()
print a.long2(123)
print a.pickup(321)
import random
print random.randint(0,100)
print random.random()
