A,B,C,D,E = [int(input()) for _ in range(5)]
ans = 0
if A <= 0:
    ans, A = -A * C + D, 0
print(ans + E*(B-A))
