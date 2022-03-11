N, M = map(int,input().split())
arr = [list(map(int,map(str,input().strip()))) for _ in range(N)]
max_num = 0


for bit in range(1 << (N*M)):
    # 수평 방향 덧셈 (비트가 0인 부분)
    total = 0
    for i in range(N):
        total_row = 0
        for j in range(M):
            index = i*M + j
            if bit & (1 << index) == 0:
                total_row = total_row*10 + arr[i][j]
            else:
                total += total_row
                total_row = 0
        total += total_row

    # 수직 방향 덧셈 (비트가 1인 부분)
    for j in range(M):
        total_col = 0
        for i in range(N):
            index = i* M+ j
            if bit & (1 << index) != 0:
                total_col = total_col*10 + arr[i][j]
            else:
                total += total_col
                total_col = 0
        total += total_col
    max_num = max(max_num, total)

print(max_num)
