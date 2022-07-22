from itertools import product
a = [1,2]
b = [3,4]
produto = list(product(a,b)) # product faz a combinação dos elementos dentro de a com os elementos de b
#[(1, 3), (1, 4), (2, 3), (2, 4)]
print(produto)