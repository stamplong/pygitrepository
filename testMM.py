import random
import os
capitals = {'hunan':'changsha','beijing':'beijing','jiangxi':'nanchang','hubei':'wuhan','zhongguo':'china'}

dic_keys = capitals.keys()
dic_values = capitals.values()
path = os.getcwd()
if os.path.exists("/Users/admin/pygitrepository/papers")==False:
    os.makedirs('/Users/admin/pygitrepository/papers')
else:
    pass
for index,name in enumerate(dic_keys):
    print "the %d paper"%index
