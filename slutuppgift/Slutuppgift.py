import random


lista = []
mainstats = []
substats = []
allstats = []

mräknare1 = 0
mräknare2 = 0
eräknare1 = 0
eräknare2 = 0
eräknare3 = 0
eräknare4 = 0
eräknare5 = 0

fortsätt = []

count = 0
countsub = 0

mainstatökning = 15
mainstatökningflat = 50
substatökning = 8


randomstatflat = [17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
randomstatökning = [5,6,7,8,9,10]
randomstatöcrtcha = [6,7,8,9]
randomstatöcrtdmg = [7,8,9,10,11,12,13,14,15]
randomstatöspd = [9,10,11,12,13,14]

randomradnomstatflat = random.choice(randomstatflat)
randomstatprocent = random.choice(randomstatökning)
randomstatcrtcha = random.choice(randomstatöcrtcha)
randomstatcrtdmg = random.choice(randomstatöcrtdmg)
randomstatspd = random.choice(randomstatöspd)


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

#for i in range(0,7):
#    randomstat = random.choice(stats)

inp1 = '0'

while inp1 != '2':
    print('')
    print('1 för att generera engravement kristall')
    print('2 för att stänga programmet')
    print('')
    inp1 = input('Vad vill du göra: ')
    
    if inp1 == '1':

        while count <= 1:
            randomradnomstatflat = random.choice(randomstatflat)
            randomstatprocent = random.choice(randomstatökning)
            randomstatcrtcha = random.choice(randomstatöcrtcha)
            randomstatcrtdmg = random.choice(randomstatöcrtdmg)
            randomstatspd = random.choice(randomstatöspd)
            randomstat = random.choice(stats)
            if randomstat not in mainstats:
                mainstats.append(randomstat)
                mainstats.append(mainstatökning)
                allstats.append(randomstat)
                allstats.append(mainstatökning)
                count = count + 1


        while countsub <= 4:
            randomradnomstatflat = random.choice(randomstatflat)
            randomstatprocent = random.choice(randomstatökning)
            randomstatcrtcha = random.choice(randomstatöcrtcha)
            randomstatcrtdmg = random.choice(randomstatöcrtdmg)
            randomstatspd = random.choice(randomstatöspd)
            randomstat = random.choice(stats)
            if randomstat not in allstats:
                substats.append(randomstat)
                substats.append(randomstatprocent)
                allstats.append(randomstat)
                allstats.append(mainstatökning)
                countsub = countsub + 1


        print('Engravement crystal current stats')
        print(mainstats)
        print(substats)

        print(' ')
        print('Type "1" if throw away crystal')
        print('Type "2" if upgrade to max level')
        print('Type "3" if you wish restart the program')
        inp = '0'
        inp = input('What to do with the crystal? ')

        while inp != '3':
    
            if inp == '1':
                print('You have successfully gotten rid of your crystal :D')

            elif inp == '2':
                print('Maxed stats:')
                print('Här ska uppgraderade stats va')

            elif inp == '3':
                break

            else:
                print('Invalid command')



#    print('Engravement crystal current stats')
#    print(mainstats)
#    print(substats)

#    print(' ')
#    print('Type "1" if throw away crystal')
#    print('Type "2" if upgrade to max level')
#    inp = input('What to do with the crystal? ')




#            print(count)
#            print(mainstats)
    
    
#     for x in stats:
# #        randomstat
#         if randomstat in mainstats:
#             print('Finns redan')
            
#         else:
#             mainstats.append(randomstat)
#             mainstats.append(mainstatökning)


    # mainstats.append(randomstat)
    # mainstats.append(mainstatökning)
        



#for i in range(0,2):   #Mainstats
#    randomstat = random.choice(stats)
#    randomradnomstatflat = random.choice(randomstatflat)
#    randomstatprocent = random.choice(randomstatökning)
#    randomstatcrtcha = random.choice(randomstatöcrtcha)
#    randomstatcrtdmg = random.choice(randomstatöcrtdmg)
#    randomstatspd = random.choice(randomstatöspd)
    
#    if randomstat == stats[0]:
#        for i in range(0,5):
#            if (mainstats == 'ATK%'):
#                print('finns redan')
#            while randomstat == 'ATK%':
#                randomstat
#                if randomstat != 'ATK%':
#                    mainstats.append(randomstat)
#                    mainstats.append(mainstatökning)
                


#                random.choice(stats)
#                if random.choice(stats) == 'ATK%':
#                    continue
#                else:
#                    print('fem')
#                    break
#            else:
#                mainstats.append(randomstat)
#                mainstats.append(mainstatökning)

#    elif randomstat == stats[1]:
#        for i in mainstats:
#            if (mainstats == 'ATK+'):
#                print('hej')

# #            else:
# {                mainstats.append(randomstat)
#                 mainstats.append(mainstatökning)

#     elif randomstat == stats[2]:
#         for i in mainstats:
#             if (mainstats == 'VIT%'):
#                 print('hej')

#             else:
#                 mainstats.append(randomstat)
#                 mainstats.append(mainstatökning)

#     elif randomstat == stats[3]:
#         for i in mainstats:
#             if (mainstats == 'VIT+'):
#                 print('hej')

#             else:
#                 mainstats.append(randomstat)
#                 mainstats.append(mainstatökning)

#     elif randomstat == stats[4]:
#         for i in mainstats:
#             if (mainstats == 'MDEF%'):
#                 print('hej')

#             else:
#                 mainstats.append(randomstat)
#                 mainstats.append(mainstatökning)

#     elif randomstat == stats[5]:
#         for i in mainstats:
#             if (mainstats == 'MDEF+'):
#                 print('hej')

#             else:
#                 mainstats.append(randomstat)
#                 mainstats.append(mainstatökning)

#     elif randomstat == stats[6]:
#         for i in mainstats:
#             if (mainstats == 'PDEF%'):
#                 print('hej')

#             else:
#                 mainstats.append(randomstat)
#                 mainstats.append(mainstatökning)

#     elif randomstat == stats[7]:
#         for i in mainstats:
#             if (mainstats == 'PDEF+'):
#                 print('hej')

#             else:
#                 mainstats.append(randomstat)
#                 mainstats.append(mainstatökning)

#     elif randomstat == stats[8]:
#         for i in mainstats:
#             if (mainstats == 'CRTCHA%'):
#                 print('hej')

#             else:
#                 mainstats.append(randomstat)
#                 mainstats.append(mainstatökning)

#     elif randomstat == stats[9]:
#         for i in mainstats:
#             if (mainstats == 'CRTDMG%'):
#                 print('hej')

#             else:
#                 mainstats.append(randomstat)
#                 mainstats.append(mainstatökning)
#     else:
#         for i in mainstats:
#             if (mainstats == 'SPD+'):
#                 print('hej')

#             else:
#                 mainstats.append(randomstat)
#                 mainstats.append(mainstatökning)


# for i in range(0,5):   #Substats
#     randomstat = random.choice(stats)
#     randomradnomstatflat = random.choice(randomstatflat)
#     randomstatprocent = random.choice(randomstatökning)
#     randomstatcrtcha = random.choice(randomstatöcrtcha)
#     randomstatcrtdmg = random.choice(randomstatöcrtdmg)
#     randomstatspd = random.choice(randomstatöspd)

#     if randomstat == stats[0]:
#         substats.append(randomstat)
#         substats.append(randomstatprocent)

#     elif randomstat == stats[1]:
#         substats.append(randomstat)
#         substats.append(randomradnomstatflat)

#     elif randomstat == stats[2]:
#         substats.append(randomstat)
#         substats.append(randomstatprocent)

#     elif randomstat == stats[3]:
#         substats.append(randomstat)
#         substats.append(randomradnomstatflat)

#     elif randomstat == stats[4]:
#         substats.append(randomstat)
#         substats.append(randomstatprocent)

#     elif randomstat == stats[5]:
#         substats.append(randomstat)
#         substats.append(randomradnomstatflat)

#     elif randomstat == stats[6]:
#         substats.append(randomstat)
#         substats.append(randomstatprocent)

#     elif randomstat == stats[7]:
#         substats.append(randomstat)
#         substats.append(randomradnomstatflat)

#     elif randomstat == stats[8]:
#         substats.append(randomstat)
#         substats.append(randomstatcrtcha)

#     elif randomstat == stats[9]:
#         substats.append(randomstat)
#         substats.append(randomstatcrtdmg)

#     else:
#         substats.append(randomstat)
#         substats.append(randomstatspd)

  
# #for i in range(0,5):
# #    randomstat = random.choice(stats)
# #    substats.append(randomstat)
