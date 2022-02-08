n, a = input().split()
total = 0
for i in range(1,int(n)+1):
    total += str(i).count(a)
print(total)