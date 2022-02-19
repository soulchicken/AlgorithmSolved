import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    li = list(map(int,input().split()))
    count = 0
    flag = True
    for i in range(n):
        if li[i] % 2 == 1:
            li[i] += 1
            
    while True:
        flag = True
        for i in range(n):
            if li[0] != li[i]:
                flag =False
        if flag: break

        for i in range(n):
            li[i] = li[i] // 2
            
        li2 = li.copy()
        for i in range(n):
            if i != n-1:
                li[i] += li2[i+1]
            else:
                li[i] += li2[0]
        
        for i in range(n):
            if li[i] % 2 == 1:
                li[i] += 1
        
        count += 1
    print(count)
        
    
    
