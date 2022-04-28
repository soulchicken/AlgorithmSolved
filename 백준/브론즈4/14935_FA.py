s = input()
for _ in range(100):
    s = str(len(s) * int(s[0]))

n = int(s)
m = len(s) * int(s[0])
if n == m: print('FA')
else: print('NFA')
