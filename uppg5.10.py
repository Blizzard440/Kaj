import datetime

dt = datetime.datetime.now()
d = dt.date()
dtext = str(d)
dttext = str(dt)
t = dt.time()
tid = str(t) [:8]

# print(dt)
# print(d)
# print(dttext)
# print(tid)
print(f'dagens datum: {d}')
print(f'Klockan är: {tid}')
