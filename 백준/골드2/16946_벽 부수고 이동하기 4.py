import sys
input = sys.stdin.readline
N, M = map(int,input().split())
check = [[True]*M for _ in range(N)]

arr = [list(map(int,list(input().strip()))) for _ in range(N)]

counts = [[0]*M for _ in range(N)]

stack = []
stack2 = []
move = ((0,1),(0,-1),(1,0),(-1,0))

def CheckIndex(i,j):
    if i >= 0 and i < N and j >= 0 and j < M:
        return True
    return False
num = 0
num_list = [0]
for i in range(N):
    for j in range(M):
        if check[i][j] and arr[i][j] == 0:
            num += 1
            count = 0
            stack.append((i,j))
            while stack:
                n,m = stack.pop()
                if CheckIndex(n,m) and check[n][m] and arr[n][m] == 0:
                    stack2.append((n,m))
                    check[n][m] = False
                    count += 1
                    for x,y in move:
                        stack.append((n+x,m+y))
            while stack2:
                n,m = stack2.pop()
                counts[n][m] = num

            num_list.append(count)

            
        elif check[i][j] and arr[i][j] == 1:
            check[i][j] = False



for i in range(N):
    for j in range(M):
        if counts[i][j] == 0:
            index = []
            for x,y in move:
                if CheckIndex(i+x,j+y):
                    index.append(counts[i+x][j+y])
            count = 1
            for a in set(index):
                count += num_list[a]
            arr[i][j] = count % 10
for i in arr:
    print(''.join(map(str,i)))
