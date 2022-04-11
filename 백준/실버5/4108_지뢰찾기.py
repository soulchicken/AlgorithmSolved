move = ((1,0),(1,1),(1,-1),(0,1),(0,-1),(-1,0),(-1,1),(-1,-1))

def check(x,y,n,m):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    return True

while 1:
    n,m = map(int,input().split())
    if n + m == 0:
        break
    li = [list(input()) for _ in range(n)]
    ans = [['*']*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            count = 0
            if li[i][j] == '*':
                continue
            for x,y in move:
                if check(i+x,j+y,n,m) and li[i+x][j+y] == '*':
                    count += 1
            ans[i][j] = str(count)
            
    for i in ans:
        print(''.join(i))
