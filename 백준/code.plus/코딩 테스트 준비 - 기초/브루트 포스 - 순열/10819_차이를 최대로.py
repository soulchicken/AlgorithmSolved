from itertools import permutations as per
n = int(input())
li = list(map(int,input().split()))
answer = 0
for pick in per(li,n):
    total = 0
    for i in range(n-1):
        total += abs(pick[i+1] - pick[i])
    answer = max(total,answer)
print(answer)