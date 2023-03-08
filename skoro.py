x = 72738-23886+22038
lista = []
for y in range(10):
    x *= 1.1
    lista.append(x)
print(lista)

lista_2 = []
for y in range(1,10):
    e = lista[y]
    e/=1.15**y
    lista_2.append(e)

print(lista_2)
print(lista[-1]*10*0.8)
dd = sum(lista_2)
kd = lista[-1]
dd += kd*10/1.15**10
print(dd*0.8)