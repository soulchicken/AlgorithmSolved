S = input()
P = input()
P_len = len(P)
S_len = len(S)
P_check = [0]*P_len
i = 1
j = 0
count = 0

for i in range(1,P_len):
    while j > 0 and P[i] != P[j]:
        j = P_check[j - 1]

    if P[i] == P[j]:
        j += 1
        P_check[i] = j

j = 0
flag = True

for i in range(S_len):
    while j > 0 and S[i] != P[j]:
        j = P_check[j - 1]

    if S[i] == P[j]:
        if j == P_len - 1:
            flag = False
            break
        else:
            j += 1
if flag: print(0)
else: print(1)
