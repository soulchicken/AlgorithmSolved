n = int(input())
li = [float('inf')]*max(n+1,6)
li[0],li[2],li[4],li[5] = 0,1,2,1
for i in range(6,n+1):
    x = min(li[i-2],li[i-5])
    if x != float('inf'):
        li[i] = x+1
if li[n] == float('inf'): print(-1)
else: print(li[n])