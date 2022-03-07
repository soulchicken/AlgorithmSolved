N, M = map(int,input().split())
li = [i+1 for i in range(N)]
stack_num = []
def DFS(depth):
    if depth == M:
        for i in stack_num:
            print(i, end = ' ')
        print()
        return
    for i in range(N):
        stack_num.append(li[i])
        DFS(depth+1)
        stack_num.pop()
DFS(0)
