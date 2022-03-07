N, M = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
check = [True]*N
stack_num = []
def DFS(depth):
    if depth == M:
        for i in stack_num:
            print(i, end = ' ')
        print()
        return
    for i in range(N):
        if check[i]:
            check[i] = False
            stack_num.append(li[i])
            DFS(depth+1)
            stack_num.pop()
            check[i] = True
DFS(0)
