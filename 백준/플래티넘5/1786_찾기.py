T = input()
P = input()
P_check = [0]*len(P)
P_len = len(P)
T_len = len(T)

j = 0
i = 1
while i < P_len:
    if P[i] == P[j]:
        j += 1
        P_check[i] = j
        i += 1
    else:
        if j != 0:
            j = P_check[j-1]
        else:
            P_check[i] = 0
            i += 1
i = 0
j = 0
count = 0
li = []
while i < T_len:
    if P[j] == T[i]:
        i += 1
        j += 1
    elif P[j] != T[i]:
        if j != 0:
            j = P_check[j-1]
        else:
            i += 1
    if j == P_len:
        li.append(i-j+1)
        count += 1
        j = P_check[j-1]
print(count)
print(' '.join(map(str,li)))
