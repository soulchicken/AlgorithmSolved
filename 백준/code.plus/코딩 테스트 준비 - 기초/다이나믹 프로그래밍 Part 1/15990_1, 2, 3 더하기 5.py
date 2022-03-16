import sys
input = sys.stdin.readline
n = int(input())
last_1 = [0,1,0,1] + [None]*100000
last_2 = [0,0,1,1] + [None]*100000
last_3 = [0,0,0,1] + [None]*100000
last_point = 3
mod = 1000000009
for _ in range(n):
    t = int(input())
    if last_1[t] == None:
        for i in range(last_point+1,t+1):
            last_1[i] = (last_2[i-1] + last_3[i-1]) % mod
            last_2[i] = (last_1[i-2] + last_3[i-2]) % mod
            last_3[i] = (last_1[i-3] + last_2[i-3]) % mod
        last_point = t
    print((last_1[t] + last_2[t] + last_3[t])% mod)
