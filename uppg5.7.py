a = ' Erik Andersson 990314-2714 '


a = a.strip()
i = a.rfind(' ')+1
j = a.find('-')
b = a[i:j]

y = b[0:2]
m = b[2:4]
d = b[4:6]

datum = d + '-' + m + '/' + y

print(datum)