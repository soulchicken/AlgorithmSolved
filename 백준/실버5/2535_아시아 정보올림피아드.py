li = []
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    li.append((c,a,b))
li.sort(reverse=True)
count = 0
i = 0
country = []
while count != 3:
    if country.count(li[i][1]) < 2:
        print(li[i][1],li[i][2])
        country.append(li[i][1])
        count += 1
    i += 1