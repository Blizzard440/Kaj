t = input(str('Skriv en text: '))

r = 0
b = 0

for c in t:
    if c == ' ' or c == '\t':
        b = r
    r = r + 1
    
if b > 0:
    print(f'sista vita tecknet fins på plats nr {b}')
else:
    print('Inget vitt tecken')
