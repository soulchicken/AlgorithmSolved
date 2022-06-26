n = int(input())
for _ in range(int(input())):
    a,b = map(int,input().split())
    n -= a*b
print('No' if n else 'Yes')