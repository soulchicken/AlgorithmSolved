dic = {}
for _ in range(int(input())):
    a,b = input().split('.')
    if b not in dic:
        dic.setdefault(b, 1)
    else:
        dic[b] += 1
dic = list(zip(dic.keys(), dic.values()))
dic.sort()
for x,y in dic:
    print(x,y)
