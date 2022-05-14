n,m = map(int,input().split())
li = [input() for _ in range(n)]
flag = True

for i in range(n):
    s = ""
    for j in range(m):
        s += li[i][j]*2
    if s != input():
        flag = False
if flag: print("Eyfa")
else: print("Not Eyfa")
