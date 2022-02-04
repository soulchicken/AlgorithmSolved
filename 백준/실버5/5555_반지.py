import sys
input = sys.stdin.readline
s = input().rstrip()
t = 0
for _ in range(int(input())):
    a = input().rstrip()*2
    if a.find(s) != -1:
        t += 1
print(t)