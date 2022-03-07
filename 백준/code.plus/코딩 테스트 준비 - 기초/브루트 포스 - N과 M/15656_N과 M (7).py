N, M = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
stack_num = []
def DFS(depth,index):
    if depth == M:
        for i in stack_num:
            print(i, end = ' ')
        print()
        return
    for i in range(index,N):
        stack_num.append(li[i])
        DFS(depth+1,index)
        stack_num.pop()
DFS(0,0)
