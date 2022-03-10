import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
answer = [-10000000]
stack = []
def DFS(i,j,total,depth):
    if depth == K:
        if answer[0] < total:
            answer[0] = total
        return
    
    for m in range(j+2,M):
        if (i-1,m) not in stack:
            stack.append((i,m))
            DFS(i,m,total+arr[i][m],depth+1)
            stack.pop()
            
    for n in range(i+1,N):
        for m in range(M):
            if (n-1,m) not in stack and ((n == i+1 and m != j) or n != i+1):
                stack.append((n,m))
                DFS(n,m,total+arr[n][m],depth+1)
                stack.pop()
    return  
                    
for i in range(N):
    for j in range(M):
        stack.append((i,j))
        DFS(i,j,arr[i][j],1)
        stack.pop()
print(answer[0])
