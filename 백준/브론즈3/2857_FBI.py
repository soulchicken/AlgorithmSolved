li = []
for i in range(1,6):
    s = input()
    if 'FBI' in s:
        li.append(str(i))
if li:
    print(' '.join(li))
else:
    print('HE GOT AWAY!')
