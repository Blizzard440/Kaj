inp = input('Heltal som ska bli max:')
a = []
räknare = 0

for i in range(0, int(inp)):
    a.append([])
    for j in range(0, 10): 
        a[i].append((i+1) * (j+1))


for rad in a:
    print(a[räknare][-1])
    räknare = räknare + 1
