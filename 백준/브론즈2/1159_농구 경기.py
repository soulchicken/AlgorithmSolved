dic = dict()
n = set()
for _ in range(int(input())):
    s = input()
    f = s[0]
    if f in dic:
        dic[f].append(s)
        if len(dic[f]) > 4:
            n.add(f)
    else:
        dic[f] = [s]
        
    
if n:
    print(''.join(sorted(list(n))))
else:
    print('PREDAJA')
