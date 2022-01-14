inp = input('Heltal som ska bli max:')
a = []
räknare = 0

for i in range(0, int(inp)):
    a.append([])
    for j in range(0, int(inp)):
        a[i].append((i+1) * (j+1))

for tal in a:
    print(a[räknare])
    räknare = räknare + 1