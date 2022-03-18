N = int(input())
P = [0] + list(map(int,input().split()))
for i in range(2,N+1):
    for j in range(1,i):
        P[i] = max(P[i], P[j] + P[i-j])
print(P[-1])
