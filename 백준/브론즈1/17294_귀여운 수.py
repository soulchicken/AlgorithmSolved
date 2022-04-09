s = list(map(int,input()))
flag = True
if len(s) != 1:
    gap = s[1] - s[0]
    for i in range(len(s) - 1):
        if s[i+1] - s[i] != gap:
            flag = False
if flag:
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
else:
    print('흥칫뿡!! <(￣ ﹌ ￣)>')
