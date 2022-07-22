from collections import deque
d = deque()

d.append(1)
d.append(2)
d.appendleft(3)
d.extend([4,5,6])#estende o deque adicionado os elementos de uma lista para a esquerda
d.rotate(1)#posisiona os elementos 1 ao lado direito
#d.rotate(-1)#posisiona os elementos 1 ao lado esquerdo
print(d)