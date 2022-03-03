li = [1,1,2]
for _ in range(3,11):
    li.append(li[-1]+li[-2]+li[-3])
for _ in range(int(input())):
    print(li[int(input())])
