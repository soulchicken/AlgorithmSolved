import sys
input = sys.stdin.readline
R, C = map(int,input().split())

def ORD(a):
    return ord(a) - 65

arr = []
for _ in range(R):
    s = list(map(ORD,input().strip()))
    arr.append(s)

count = 0
check = [True]*26
check[arr[0][0]] = False
move = ((0,1),(0,-1),(1,0),(-1,0))

def DFS(x,y,depth):
    global count
    if depth > count:
        count = depth
    for i,j in move:
        if x + i >= 0 and x + i < R and y + j >= 0 and y + j < C:
            n = arr[x+i][y+j]
            if check[n]:
                check[n] = False
                DFS(x+i,y+j,depth+1)
                check[n] = True
DFS(0,0,1)
print(count)
