L,C = map(int,input().split())
li = sorted(list(input().split()))
check = [True]*C
stack = []
def DFS(vow,con,index,depth):
    if depth == L:
        if vow > 0 and con > 1:
            for i in stack:
                print(i,end='')
            print()
        return
    for c in range(index+1,C):
        if check[c]:
            check[c] = False
            stack.append(li[c])
            if li[c] in ['a','e','i','o','u']:
                DFS(vow+1,con,c,depth+1)
            else:
                DFS(vow,con+1,c,depth+1)            
            stack.pop()
            check[c] = True
DFS(0,0,-1,0)
