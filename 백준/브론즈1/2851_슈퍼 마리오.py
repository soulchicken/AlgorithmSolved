li = [int(input()) for _ in range(10)]
total = 0
for i in range(10):
    if total + li[i] > 100:
        if abs(total - 100) < abs(total + li[i] - 100):
            print(total)
        else:
            print(total + li[i])
        break
    total += li[i]
    if i == 9:
        print(total)
