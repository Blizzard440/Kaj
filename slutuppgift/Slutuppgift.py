import random


lista = []
mainstats = []
substats = []


mräknare1 = 0
mräknare2 = 0
eräknare1 = 0
eräknare2 = 0
eräknare3 = 0
eräknare4 = 0
eräknare5 = 0


mainstatökning = 15
mainstatökningflat = 50
substatökning = 8


randomstatflat = [17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
randomstatökning = [5,6,7,8,9,10]
randomstatöcrtcha = [6,7,8,9]
randomstatöcrtdmg = [7,8,9,10,11,12,13,14,15]
randomstatöspd = [9,10,11,12,13,14]


stats = ['ATK%', 'ATK+', 'VIT%', 'VIT+', 'MDEF%', 'MDEF+', 'PDEF%', 'PDEF+', 'CRTCHA%', 'CRTDMG%', 'SPD+']
#randomstat = random.choice(stats)


#print('Du kommer nu att få en engravement kristall med random stats')
#print(stats[1])
#print(randomstat)


#randomstat = random.choice(stats)
#randomradnomstatflat = random.choice(randomstatflat)
#randomstatprocent = random.choice(randomstatökning)
#randomstatcrtcha = random.choice(randomstatöcrtcha)
#randomstatcrtdmg = random.choice(randomstatöcrtdmg)
#randomstatspd = random.choice(randomstatöspd)


for i in range(0,2):   #Mainstats
    randomstat = random.choice(stats)
    randomradnomstatflat = random.choice(randomstatflat)
    randomstatprocent = random.choice(randomstatökning)
    randomstatcrtcha = random.choice(randomstatöcrtcha)
    randomstatcrtdmg = random.choice(randomstatöcrtdmg)
    randomstatspd = random.choice(randomstatöspd)
    
    if randomstat == stats[0]:

        mainstats.append(randomstat)
        mainstats.append(mainstatökning)

    elif randomstat == stats[1]:
        mainstats.append(randomstat)
        mainstats.append(mainstatökning)

    elif randomstat == stats[2]:
        mainstats.append(randomstat)
        mainstats.append(mainstatökning)

    elif randomstat == stats[3]:
        mainstats.append(randomstat)
        mainstats.append(mainstatökning)

    elif randomstat == stats[4]:
        mainstats.append(randomstat)
        mainstats.append(mainstatökning)

    elif randomstat == stats[5]:
        mainstats.append(randomstat)
        mainstats.append(mainstatökning)

    elif randomstat == stats[6]:
        mainstats.append(randomstat)
        mainstats.append(mainstatökning)

    elif randomstat == stats[7]:
        mainstats.append(randomstat)
        mainstats.append(mainstatökning)

    elif randomstat == stats[8]:
        mainstats.append(randomstat)
        mainstats.append(mainstatökning)

    elif randomstat == stats[9]:
        mainstats.append(randomstat)
        mainstats.append(mainstatökning)

    else:
        mainstats.append(randomstat)
        mainstats.append(mainstatökning)


for i in range(0,5):   #Substats
    randomstat = random.choice(stats)
    randomradnomstatflat = random.choice(randomstatflat)
    randomstatprocent = random.choice(randomstatökning)
    randomstatcrtcha = random.choice(randomstatöcrtcha)
    randomstatcrtdmg = random.choice(randomstatöcrtdmg)
    randomstatspd = random.choice(randomstatöspd)

    if randomstat == stats[0]:
        substats.append(randomstat)
        substats.append(randomstatprocent)

    elif randomstat == stats[1]:
        substats.append(randomstat)
        substats.append(randomradnomstatflat)

    elif randomstat == stats[2]:
        substats.append(randomstat)
        substats.append(randomstatprocent)

    elif randomstat == stats[3]:
        substats.append(randomstat)
        substats.append(randomradnomstatflat)

    elif randomstat == stats[4]:
        substats.append(randomstat)
        substats.append(randomstatprocent)

    elif randomstat == stats[5]:
        substats.append(randomstat)
        substats.append(randomradnomstatflat)

    elif randomstat == stats[6]:
        substats.append(randomstat)
        substats.append(randomstatprocent)

    elif randomstat == stats[7]:
        substats.append(randomstat)
        substats.append(randomradnomstatflat)

    elif randomstat == stats[8]:
        substats.append(randomstat)
        substats.append(randomstatcrtcha)

    elif randomstat == stats[9]:
        substats.append(randomstat)
        substats.append(randomstatcrtdmg)

    else:
        substats.append(randomstat)
        substats.append(randomstatspd)

  
#for i in range(0,5):
#    randomstat = random.choice(stats)
#    substats.append(randomstat)

print('Engravement crystal current stats')
print(mainstats)
print(substats)

print(' ')
print('Type "1" if throw away crystal')
print('Type "2" if upgrade to max level')
inp = input('What to do with the crystal? ')

if inp == '1':
    print('You have successfully gotten rid of your crystal :D')

elif inp == '2':
    print('Max')

else:
    print('Invalid command')

