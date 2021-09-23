poäng = int(input('Antal poäng på ditt prov: '))

#e = 25-29
#d = 30-34
#c = 35-39
#b = 40-44
#a = 45-50

if poäng >= 45:
    print('Betyg A')
elif poäng == d:
    print('Betyg D')
elif poäng == c:
    print('Betyg C')
elif poäng == b:
    print('Betyg B')
elif poäng == a:
    print('Betyg A')
elif poäng < e:
    print('Du fick tyvärr underkänt')
else:
    print('För högt input')