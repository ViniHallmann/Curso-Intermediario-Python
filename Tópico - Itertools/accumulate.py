from itertools import accumulate # vai somando os elementos da lista
import operator
a = [1,2,3,4]
acc = accumulate(a, func=operator.mul)#com o modulo Operator, eu posso definir que a função do accumulate vai ser de Multiplicação em vez de adição.
print(a)
print(list(acc))