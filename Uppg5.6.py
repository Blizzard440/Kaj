datum = input('skriv ett svenskt datum if formen dd/mm/åå: ')

dag = datum[:2]
mån = datum[2:4]
år = datum[4:6]

usadatum = mån + '-' + dag + '-' + '20' + år

print(f'Datumet skrivs {usadatum} i usa')