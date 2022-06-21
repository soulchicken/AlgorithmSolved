R,C,ZR,ZC = map(int,input().split())
arr = [input() for _ in range(R)]
answer = []
for i in arr:
    s = ""
    for j in i:
        s += j*ZC
    answer.append(s)
for i in answer:
    for j in range(ZR):
        print(i)
