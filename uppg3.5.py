bredd = float(input('Brevets bredd i mm: '))
längd = float(input('Brevets längd i mm: '))
tjocklek = float(input('Brevets tjocklek i mm: '))

brevtotal = bredd + längd + tjocklek

if längd > 600:
    print('Ditt brev är för långt')
elif längd < 140:
    print('Din brevlängd är för kort')
elif tjocklek > 100:
    print('Brevet är för tjock')
elif bredd < 90:
    print('Brevet är för lite brett')
elif brevtotal > 900:
    print('Ditt brev är tyvärr för stort')
else:
    print('Det är bara att skicka brevet')
