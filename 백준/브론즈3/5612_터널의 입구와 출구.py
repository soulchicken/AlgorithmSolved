import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
car = m
max_car = m
flag = True
for _ in range(n):
    if not flag:
        continue
    a,b = map(int,input().split())
    car += a - b
    if car < 0:
        flag = False
    max_car = max(car,max_car)
print(max_car if flag else 0)
