import random

tal = input('Skriv talen du vill räkna på:')
ordlista = tal.split ()
talunder0 = 0
talöver0 = 0

for t in ordlista:
    if int(t) <= 0:
        talunder0 = talunder0 + 1
    else:
        talöver0 = talöver0 + 1

print(f'{talunder0} st tal under eller lika med 0 och {talöver0} st tal över 0')