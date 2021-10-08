text = input(str('Skriv in ett slumpat ord: '))

if text[0] == text[-1]:
    print('Första och sista bokstaven är lika')
else:
    print('Första och sista bokstaven är olika')
