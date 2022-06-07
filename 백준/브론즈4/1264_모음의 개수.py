import sys
input = sys.stdin.readline
check = ['a','e','i','o','u','A','E','I','O','U']
while 1:
    t = 0
    s = input().strip()
    if s == '#':
        break
    for i in check:
        t += s.count(i)
    print(t)
