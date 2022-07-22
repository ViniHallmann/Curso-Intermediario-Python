from collections import namedtuple
#namedtuple
Point = namedtuple('Point', 'x y')# namedtuple cria uma classe e pode dar uma 'posição' para ela
pt = Point(1,-4)
print(pt.x,pt.y)
print(pt)