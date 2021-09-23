tal = input('Skriv in antalet sekunder för omvandling: ')

timme = int(tal)/3600
minut = int(tal)/60
sekund = int(tal)

print(f'{tal} sekunder är {timme} timmar, eller {minut} minuter, eller {sekund} sekunder')
