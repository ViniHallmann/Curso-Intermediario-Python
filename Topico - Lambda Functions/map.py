#map(func, seq) recebe uma função e a sequencia
a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b)) # precisa ser uma lista

#Outra maneira de escrever, com outro método
c = [x*2 for x in a]
print(c)