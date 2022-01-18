K = int(input())
check = [True]*7368788
count = 0
for i in range(2,7368789):
    if check[i]:
        count += 1
        if count == K:
            print(i)
            break
        for j in range(i*2,7368788,i):
            check[j] = False
