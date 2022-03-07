N, M = map(int,input().split())
stack_num = []
def DFS(depth,index):
    if depth == M:
        for i in stack_num:
            print(i, end = ' ')
        print()
        return
    for i in range(index,N):
        stack_num.append(i+1)
        DFS(depth+1,i)
        stack_num.pop()
DFS(0,0)
