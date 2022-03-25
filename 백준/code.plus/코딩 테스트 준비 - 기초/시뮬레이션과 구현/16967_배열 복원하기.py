import sys
input = sys.stdin.readline
H,W,X,Y = map(int,input().split())
A = [[-1]*W for _ in range(H)]
B = [list(map(int,input().split())) for _ in range(H+X)]

for i in range(H):
    if i < X:
        for j in range(W):
            A[i][j] = B[i][j]

    elif i < H - X:
        for j in range(W):
            if j < Y:
                A[i][j] = B[i][j]
            elif j < W - Y:
                A[i][j] = B[i][j] - A[i-X][j-Y]
            else:
                A[i][j] = B[i+X][j+Y]
    
    else:
        for j in range(W):
            A[i][j] = B[i+X][j+Y]
for i in A:
    print(' '.join(map(str,i)))
