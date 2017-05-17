import itertools
def yieldd ():
    for x in itertools.product([1,2,3,4],[2,3,4],[1,1,2,2,]):
        yield x
for yield_x in yieldd():
    print yield_x
