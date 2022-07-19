odds = {1,3,5,7,9}
evens = {2,4,6,8}
primes = {2,3,5,7}
#.union une os dois sets, sem duplicar os elementos
uniao = odds.union(evens)
print(uniao)

# .intersection procura a intersecção dos dois sets
intersec = odds.intersection(evens)
print(intersec)

# .difference procura o que e diferente entre os dois sets
dif = evens.difference(primes)
print(dif)

# .update atualiza o set com os elementos de um outro set sem duplicar
odds.update(evens)
print(odds)
# o método .upadte pode ser usado nos outros métodos acima #

setA = {1,2,3,4,5,6}
setB = {1,2,3}
# .issubset quer saber se o que contem dentro de um setX esta contido tambem em um setY
print(setA.issubset(setB)) # Nesse caso retorna False pois o setA possui mais elementos que o setB
print(setB.issubset(setA)) # Se invertermos o método, ele sera True pois todo elemento do setB esta contido no setA

# .issuperset e o oposto to issubset. Retorna True se o primeiro setX contem todos os elementos do segundo setY
print(setA.issuperset(setB)) # Nesse caso, o retorno sera True pois o setA possui todos os elementos do setB
print(setB.issuperset(setA)) # E nesse caso vai retornar False por o setB nao possui todos os elementos do setA

# .isdisjoint quer saber se os dois sets nao possuem nada em comum
setC = {7,8}
print(setA.isdisjoint(setC)) # Vai retornar True pois os dois nao possuem nenhum elemento em comum

# .copy() copia um set para outro
# setB = setA.copy()
# frozenset e imutável

a = frozenset([1,2,3,4])
try: 
    a.add(5) # Isso vai dar erro pois nao da pra adicionar ou remover elementos numa frozenset
except:
    print("ERRO, nao foi possivel adicionar 1 ao frozenset")
print(a)
