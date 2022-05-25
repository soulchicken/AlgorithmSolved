import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n,m = map(int,input().split())
parent = [i for i in range(n+1)]

def find_parent(a):
    if parent[a] == a:
        return a
    
    parent[a] = find_parent(parent[a])
    return parent[a]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if b > a:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    a,x,y = map(int,input().split())
    if a:
        if find_parent(x) == find_parent(y):
            print('YES')
        else:
            print('NO')
    else:
        union(x,y)
