from itertools import combinations, combinations_with_replacement # faz a combinação dos elementos de uma lista
a = [1,2,3,4]
comb = combinations(a,2) # obrigatório ter o segundo parâmetro nessa função.
comb_wr = combinations_with_replacement(a,2) # essa função faz a combinação com números iguais 
print(list(comb))
print(list(comb_wr))