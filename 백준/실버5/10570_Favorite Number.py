import sys
input = sys.stdin.readline
for _ in range(int(input())):
    li = [0] * 1001
    for _ in range(int(input())): 
        li[int(input())] += 1
    max_num = max(li)
    for i in range(1,1001):
        if li[i] == max_num:
            print(i)
            break