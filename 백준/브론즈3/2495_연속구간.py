for _ in range(3):
    num = input()
    count = 1
    max_count = 1
    for i in range(1,len(num)):
        if num[i] == num[i-1]:
            count += 1
            max_count = max(count, max_count)
        else:
            max_count = max(count, max_count)
            count = 1
    print(max_count)
