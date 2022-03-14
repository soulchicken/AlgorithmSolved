import sys
input = sys.stdin.readline
li = [1,1,2]
for _ in range(3,1000001):
    li.append((li[-1]+li[-2]+li[-3]) % 1000000009)
for _ in range(int(input())):
    print(li[int(input())])
