from itertools import groupby

def smaller_than_3(x):
    return x < 3

a = [1,2,3,4]

group_obj = groupby(a, key=smaller_than_3)
for k,v in group_obj:
    print(k,list(v))
