li = [(int(input()), i+1) for i in range(8)]
li.sort(reverse=True)
total = 0
s = []
for i in range(5):
    total += li[i][0]
    s.append(li[i][1])
print(total)
s.sort()
for num in s:
    print(num, end = ' ')