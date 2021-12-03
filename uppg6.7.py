print('Skriv en matris rad för rad.\nAvsluta med en tom rad eller ett kommatecken.')

m = []
while True:
    s = input('? ')
    if s == '':
        break
    elif s == ',':
        break
    ls = s.split()
    rad = [float(e) for e in ls]
    m.append(rad)

print(m)
