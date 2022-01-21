import random

mräknare1 = 0
mräknare2 = 0
eräknare1 = 0
eräknare2 = 0
eräknare3 = 0
eräknare4 = 0
eräknare5 = 0


randomstatflat = [17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
randomstatökning = [5,6,7,8,9,10]
randomstatöcrtcha = [6,7,8,9]
randomstatöcrtdmg = [7,8,9,10,11,12,13,14,15]
randomstatöspd = [9,10,11,12,13,14]



print('Du kommer nu att få en engravement kristall med random stats')

stats = ['ATK%', 'ATK+', 'VIT%', 'VIT+', 'MDEF%', 'MDEF+', 'PDEF%', 'PDEF+', 'CRTCHA%', 'CRTDMG%', 'SPD+']
randomstat = random.choice(stats)
#print(stats[1])
print(randomstat)
