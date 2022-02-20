n, h, w = map(int,input().split())
li = [list(input()) for _ in range(h)]
s = [' ']*len(li[0])
for i in range(h):
    for j in range(len(li[0])):
        if s[j] == ' ' or s[j] == '?':
            s[j] = li[i][j]
s = ''.join(s)
ans = ""
for i in range(len(s)//w):
    a = s[i*w:i*w+w]
    for i in a:
        if i != "?":
            ans += i
            break
    else:
        ans += '?'
print(ans)
        
        
