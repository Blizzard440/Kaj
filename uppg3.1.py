samtalstid = float(input('Hur många minuter har du ringt denna månad? '))

pris = samtalstid * 10

reapris = pris * 0.9

if pris >= 300:
    print(f'Din samtalsräknnig denna månda är: {reapris:.1f}kr')

else:
    print(f'Din samtalsräknnig denna månda är: {pris:.1f}kr')
