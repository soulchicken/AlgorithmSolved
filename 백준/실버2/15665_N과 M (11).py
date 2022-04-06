n,m = map(int,input().split())
li = list(set(map(int,input().split())))
li.sort()
stack = []
def DFS(depth):
    if depth == m:
        print(' '.join(map(str,stack)))
        return
    for i in li:
        stack.append(i)
        DFS(depth + 1)
        stack.pop()

DFS(0)