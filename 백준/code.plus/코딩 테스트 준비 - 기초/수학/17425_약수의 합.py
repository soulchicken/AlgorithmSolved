import sys
input = sys.stdin.readline
t = int(input())
input_num = list(int(input()) for _ in range(t))
max_num = max(input_num)
li = [0]* (max_num + 1)
totals = [0]* (max_num + 1)
for i in range(1,max_num+1):
    for j in range(1,max_num//i + 1):
        if i * j <= max_num:
            li[i*j] += i
for i in range(1,max_num + 1):
    totals[i] = totals[i-1] + li[i]

for i in input_num:
    print(totals[i])