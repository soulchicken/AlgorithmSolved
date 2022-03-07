N, M = map(int,input().split())
li = [i+1 for i in range(N)]
stack_num = []


def DFS(index,depth):
    if depth == M-1:
        for i in stack_num:
            print(i, end = " ")
        print()
        return
    for i in range(index + 1, N):
        stack_num.append(li[i])
        DFS(i,depth+1)
        stack_num.pop()
    
for i in range(N):
    stack_num.append(li[i])
    DFS(i,0)
    stack_num.pop()
