n = int(input())
li = list(map(int,input().split()))
T = sum(li)
check = [0]*n
i = -1
for t in range(1,T+1):
    while 1:
        i += 1
        if i >= n:i = 0
        if li[i] == 1:
            li[i] = 0
            check[i] = str(t)
            break
        elif li[i] != 0:
            li[i] -= 1
            break       
print(' '.join(check))
