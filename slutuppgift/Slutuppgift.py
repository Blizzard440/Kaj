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


for i in range(0,2):
    randomstat = random.choice(stats)
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

    

#for i in range(0,5):
#    randomstat = random.choice(stats)
#    substats.append(randomstat)


print(mainstats)
#print(substats)