from itertools import count, cycle, repeat
for i in count(10):
    print(i)
    if i == 15:
        break

a = [1,2,3]
for i in cycle(a):# rpinta 1,2,3 varias vezes
    print(i)

for i in repeat(1, 5):# repete o 1 5 vezes
    print(i)

   