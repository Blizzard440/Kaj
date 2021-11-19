import random
lista = []
c0 = 0

for i in range(0,100):
    r = random.randint(0,3)
    lista.append(r)
    if 0 in lista:
        lista.remove(0)
        c0 = c0 + 1
print(lista)