A,B = map(int,input().split())
n = int(input())
answer = [abs(A-B)]
for _ in range(n):
    answer.append(abs(B - int(input())) + 1)
print(sorted(answer)[0])
