import math #importerar programet math

diameter = float(input('Cirkelns diameter: ')) #frågar efter storleken på cirkeln

pi = math.pi #variabel för pi
radie = diameter / 2 #uträkning av radien på cirkeln
omkrets = pi * diameter #uträkning av omkrets på cirkeln
area = pi * radie**2 #uträkning av aren på cirkeln

print(f'Cirkelns radie: {radie:.3f}\nCirkelns omkrets: {omkrets:.3f}\nCirkelns area: {area:.3f}') #utskrift av cirkelns värden
