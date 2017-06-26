class lexicon():
    def __init__(self):
        self.whole_char = {'north':'direction','south':'direction','east':'direction','west':'direction','down':'direction','up':'direction','stop':'verb','kill':'verb','eat':'verb','kell':'verb'}

    def scan(self,stuff):
        words = stuff.split()
        my_result = []
        for n in range(0,len(words)):
            c = words[n]
            a = self.charac(c)
            my_result.append(a)
        return my_result
    def charac(self,c):
        if c in self.whole_char:
            b = self.whole_char[c]
            return b,c
        else:
            return self.int_test(c)
    def int_test(self,c):
        try:
            c = int(c)
            return ('number',c)
        except:
            return('error',c)
