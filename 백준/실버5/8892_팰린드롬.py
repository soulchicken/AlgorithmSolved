import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    li = [input().rstrip() for _ in range(n)]
    flag = 0
    for i in range(n):
        if flag: continue
        for j in range(i+1,n):
            if li[i] + li[j] == (li[i] + li[j])[::-1]:
                print(li[i] + li[j])
                flag=1
                break

            if li[j] + li[i] == (li[j] + li[i])[::-1]:
                print(li[j] + li[i])
                flag=1
                break

    if not flag: print(0)
        
