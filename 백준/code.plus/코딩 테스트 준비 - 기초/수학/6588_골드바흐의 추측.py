import sys
input = sys.stdin.readline
li = [0]*1000001
li2 = []
for i in range(2,1000001):
    if li[i] == 0:
        if i % 2 == 1:
            li2.append(i)
        for j in range(i*2,1000001,i):
            li[j] = 1
while 1:
    n = int(input())
    if n == 0: break
    for i in li2:
        if li[n - i] == 0:
            print(n,"=",i,"+",n-i)
            break
