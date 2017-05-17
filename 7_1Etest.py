D = {a:345 for a in {"time":123,"month":278}}
print D

def abc(a,b,c):
    if a>b:
        g=b
        b=a
        a=g
    elif a>c:
        g=c
        c=a
        a=c
    elif b>c:
        g=c
        c=b
        b=g
    print a,b,c
abc(5,3,6)
