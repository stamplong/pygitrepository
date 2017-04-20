class song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_baby = song(["happy birthday toyou",
                    "i don't want to get sued",
                    "so i'll stop right there"])

bulls_on_parade = song(["they rally around tha family"])

happy_baby.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
