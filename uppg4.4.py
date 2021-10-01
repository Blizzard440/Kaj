start = float(input('Bollens höjd: '))

stop = 1
studs = 0

while start > stop:
    start = start * 0.7
    studs = studs + 1

print('Antal studs', studs)