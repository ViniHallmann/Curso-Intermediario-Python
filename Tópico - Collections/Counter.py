from collections import Counter
#Counter
a = "aaaaabbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys())
print(my_counter.items())
print(my_counter.values())
print(my_counter.most_common())
print(list(my_counter.elements()))# precisa transformar em uma lista para usar o .elements e ver todos os elementos da variavel