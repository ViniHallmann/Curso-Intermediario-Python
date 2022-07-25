from itertools import permutations # muda a ordem do output
a = [1,2,3]
perm = permutations(a)
perm = permutations(a, 2)#O numero dois mostra so a permutacao de dois numeros da lista
print(list(perm))