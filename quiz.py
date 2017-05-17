import random
capitals = {'hunan':'changsha','beijing':'beijing','jiangxi':'nanchang','hubei':'wuhan','zhongguo':'china'}
x = list(capitals.keys())

y = list(capitals.values)
z = y[:]
random.shuffle(y)

for number in range(5):  #five question
    print x[number]
    print ("where is %s 's city"%x[number])

    correct_answer = z[number]
    string_correct_answer = str(correct_answer)
    total_answer.append(z[0:2])
    total_answer.append(string_correct_answer)
    print total_answer

    for w in range(4):
        print "ABCD"[number],
        print answer
