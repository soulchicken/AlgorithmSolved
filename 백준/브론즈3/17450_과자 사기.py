a = 'SNU'
max_num = 0
index = 0
for i in range(3):
    x,y = map(int,input().split())
    x *= 10
    y *= 10
    if x >= 5000:
        x -= 500
    if y/x > max_num:
        max_num = y/x
        index = i
print(a[index])
