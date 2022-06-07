li = [0,1,1,1]
for _ in range(100):
    li.append(li[-2] + li[-3])
for _ in range(int(input())):
    print(li[int(input())])
