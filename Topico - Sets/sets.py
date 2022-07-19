# Sets: sem ordem, mutáveis e sem itens duplicados
myset = {1,2,3,1,2,3}
print(myset)
myset2 = set("HELLO")
print(myset2)

# Para adicioanar itens ao set, usamos o metodo .add
    #myset.add(4)
# Descarta todo os elementos iguais ao que está dentro do ()
    #myset.discard(3)
# Limpa tudo dentro do set
    #myset.clear()

if 1 in myset:
    print('O numero 1 esta no set')
