poly = input()
count = 0
flag = True
answer = ''
i = 0
while 1:
    if i == len(poly):
        if count % 2 == 1:
            flag = False
        elif count == 4:
            answer += 'AAAA'
        elif count == 2:
            answer += 'BB'
        break

    if poly[i] == '.':
        if count % 2 == 1:
            flag = False
            break
        elif count == 4:
            answer += 'AAAA'
        elif count == 2:
            answer += 'BB'
        answer += '.'
        count = 0
        i += 1
        continue
    else:
        count += 1
        if count == 4:
            answer += 'AAAA'
            count = 0
        
    i += 1
if flag: print(answer)
else: print(-1)
