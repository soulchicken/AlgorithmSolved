li = [True]*1000001
check = []
for i in range(2,1000001):
    if li[i]:
        check.append(i)
        for j in range(i*2,1000001,i):
            li[j] = False

n = int(input())
for _ in range(n):
    num = int(input())
    for i in check:
        if num % i == 0:
            print('NO')
            break
    else:
        print('YES')
