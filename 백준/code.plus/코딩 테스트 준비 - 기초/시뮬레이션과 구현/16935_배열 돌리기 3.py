import sys
import copy
input = sys.stdin.readline
N, M, R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
li = list(map(int,input().split()))
for i in li:
    if i == 1:
        N = len(arr)
        M = len(arr[0])
        for n in range(N//2):
            arr[n], arr[N - 1 - n] = arr[N - 1 - n], arr[n]
    elif i == 2:
        N = len(arr)
        M = len(arr[0])
        for n in range(N):
            for m in range(M//2):
                arr[n][m], arr[n][M - 1 - m] = arr[n][M - 1 - m], arr[n][m]

    elif i == 3:
        tmp = [[0]*len(arr) for _ in range(len(arr[0]))]
        for n in range(len(arr[0])):
            for m in range(len(arr)):
                tmp[n][m] = arr[len(arr) - 1 - m][n]
        arr = copy.deepcopy(tmp)

    elif i == 4:
        tmp = [[0]*len(arr) for _ in range(len(arr[0]))]
        for n in range(len(arr[0])):
            for m in range(len(arr)):
                tmp[n][m] = arr[m][len(arr[0]) - 1 - n]
        arr = copy.deepcopy(tmp)

    else:
        col = len(arr)//2
        row = len(arr[0])//2
        tmp1 = [[0]*row for _ in range(col)]
        tmp2 = copy.deepcopy(tmp1)
        tmp3 = copy.deepcopy(tmp1)
        tmp4 = copy.deepcopy(tmp1)

        for n in range(col):
            for m in range(row):
                tmp1[n][m] = arr[n][m]
                tmp2[n][m] = arr[n][m + row]
                tmp4[n][m] = arr[n + col][m]
                tmp3[n][m] = arr[n + col][m + row]
        if i == 5:
            for n in range(col):
                for m in range(row):
                    arr[n][m] = tmp4[n][m]
                    arr[n][m + row] = tmp1[n][m]
                    arr[n + col][m] = tmp3[n][m]
                    arr[n + col][m + row] = tmp2[n][m]
        else:
            for n in range(col):
                for m in range(row):
                    arr[n][m] = tmp2[n][m]
                    arr[n][m + row] = tmp3[n][m]
                    arr[n + col][m] = tmp1[n][m]
                    arr[n + col][m + row] = tmp4[n][m]

for i in arr:
    for j in i:
        print(j, end = ' ')
    print()
