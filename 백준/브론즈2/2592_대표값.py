li = [0]*1001
total = 0
for _ in range(10):
    n = int(input())
    li[n] += 1
    total += n
print(total//10)
print(li.index(max(li)))
