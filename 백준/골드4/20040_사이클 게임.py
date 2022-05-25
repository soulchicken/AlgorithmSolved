import sys
input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n)]

ans = [0]

def find_parent(a):
    if parent[a] == a:
        return a
    
    parent[a] = find_parent(parent[a])
    return parent[a]

def union(i, a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        if b > a:
            parent[b] = a
        else:
            parent[a] = b

    elif ans[0] == 0:
        ans[0] = i+1

for i in range(m):
    a,b = map(int,input().split())
    union(i, a, b)
print(ans[0])
