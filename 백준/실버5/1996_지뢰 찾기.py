n = int(input())
li = [list(input()) for _ in range(n)]

ans = [[0]*n for _ in range(n)]
def check_index(i,j):
    if 0 <= i < n and 0 <= j < n and li[i][j] != '.':
        return True
    return False

x = [1,1,1,0,0,-1,-1,-1]
y = [-1,0,1,-1,1,-1,0,1]

for i in range(n):
    for j in range(n):
        if li[i][j] != '.':
            ans[i][j] = '*'
            continue
        count = 0
        for k in range(8):
            if check_index(i+x[k],j+y[k]):
                count += int(li[i+x[k]][j+y[k]])

        if count < 10:
            ans[i][j] = count
        else:
            ans[i][j] = 'M'

for i in ans:
    print(''.join(map(str,i)))
