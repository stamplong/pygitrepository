foods = {'Alice':{'apple':5,'dog':3},
        'jason':{'apple':2,'dog':2}}
print 'Alice' in foods
print 'Alice' in foods.keys()

total = 0
for x,v in foods.items():
    total = total + v.get('dog',0)
print total
def totalfood (food,item):
    total_1 = 0
    for x,v in food.items():
        total_1 = total_1 + v.get(item,0)
    return total_1
print totalfood(foods,'apple')
