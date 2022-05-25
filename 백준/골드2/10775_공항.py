import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)
G = int(input())
P = int(input())

parent = [i for i in range(G+1)]

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

ans = 0
for _ in range(P):
    g = int(input())
    p = find_parent(g)
    if not p:
        break
    union(p,p - 1)
    ans += 1
print(ans)
