#reduce(func,seq)
from functools import reduce
a = [1,2,3,4]

produto_a = reduce(lambda x,y: x*y,a)
print(produto_a)