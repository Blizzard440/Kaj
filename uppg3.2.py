besök = int(input('Hur många besök förväntar du dig göra under ett år? '))

biljett = 150
biljettår = besök * biljett
årskort = 5600

if biljettår >= årskort:
    print('Årskort blir billigare')

else:
    print('Biljetter blir billigare')
