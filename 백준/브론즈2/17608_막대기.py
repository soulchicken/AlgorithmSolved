max_num = 0
count = 0
m = int(input())
li = [int(input()) for _ in range(m)]
for i in range(len(li)-1,-1,-1):
    n = li[i]
    if n > max_num:
        count += 1
        max_num = n
print(count)
