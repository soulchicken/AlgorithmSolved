li = [1,1]
li2 = [1,1]
n = 1
for i in range(2,10001):
    n = int((str(n*i).rstrip('0'))[-5:])
    li.append(n)
    li2.append(n % 10)
    answer = []
max_len = 0
while 1:
    try:
        n = int(input())
        answer.append(f'{n} -> {li2[n]}')
        max_len = max(len(f'{n} -> {li2[n]}'),max_len)
    except:
        break
for i in answer:
    print(i.rjust(max_len+1))
