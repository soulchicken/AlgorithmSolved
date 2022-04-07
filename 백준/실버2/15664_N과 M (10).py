n,m = map(int,input().split())
li = list(map(int,input().split()))
num = [0]*10001
for i in li:
    num[i] += 1

stack = []

def DFS(index,depth):

    if depth == m:
        print(' '.join(map(str,stack)))
        return
    for i in range(index,len(num)):
        for j in range(min(num[i], m - depth),0,-1):
            for _ in range(j):
                stack.append(i)
            num[i] -= j
            DFS(i + 1, depth + j)
            num[i] += j
            for _ in range(j):
                stack.pop()          

DFS(0,0)
