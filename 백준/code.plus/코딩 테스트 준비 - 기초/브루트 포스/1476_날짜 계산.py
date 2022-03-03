e,s,m = map(int,input().split())
E,S,M = 0,0,0
count = 0
while not (E == e and S == s and M == m):
    E += 1
    S += 1
    M += 1
    count += 1
    if E == 16:
        E = 1
    if S == 29:
        S = 1
    if M == 20:
        M = 1
print(count)
