a = input()
count = 0
while len(a) != 1:
    count += 1
    a = list(map(int,a))
    a = str(sum(a))

a = int(a)
print(count)
if a in [3,6,9]:
    print('YES')
else:
    print('NO')