n = int(input())
count = 0
for i in range(1,n):
    n -= i
    if n < 0:
        break
    count += 1
print(count)