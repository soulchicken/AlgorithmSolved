n = int(input())
stick = [64,32,16,8,4,2,1]
count = 0
for i in stick:
    if n >= i:
        n -= i
        count += 1
print(count)