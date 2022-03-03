li = []
sum = - 100
for _ in range(9):
    n = int(input())
    li.append(n)
    sum += n
flag = True
for i in range(9):
    if flag:
        for j in range(i+1,9):
            if li[i] + li[j] == sum:
                flag = False
                li.pop(j)
                li.pop(i)
                break
li.sort()
for i in li:
    print(i)