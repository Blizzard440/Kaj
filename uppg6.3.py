import random

lista = []
c = 0

for i in range(0,100):
    r = random.randint(1,1000)
    lista.append(r)
    lista.sort()
    c = c + 1
medelvärde = sum(lista)//c

print('Största talet:',lista[-1])
print('Minsta värdet:',lista[0])
print('Medelvärde',medelvärde)
