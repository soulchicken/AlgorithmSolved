S = input()
K = input()
j = 0
T = ''
for i in S:
    if i.isalpha():T += i
K_len = len(K)
T_len = len(T)
K_check = [0]*K_len
j = 0

# check point
for i in range(1,K_len):
    if K[i] == K[j]:
        j += 1
        K_check[i] = j
    else:
        j = 0

# check KMP!

# 다른 문제 코드
j = 0
flag = True

for i in range(T_len):
    while j > 0 and T[i] != K[j]:
        j = K_check[j - 1]

    if T[i] == K[j]:
        if j == K_len - 1:
            flag = False
            break
        else:
            j += 1
if flag: print(0)
else: print(1)
