for i in range(int(input())):
    start, end = map(int,input().split())
    zero = 0
    for j in range(start,end+1):
        zero += str(j).count('0')
    print(zero)
