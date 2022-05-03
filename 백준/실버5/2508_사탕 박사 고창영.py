for _ in range(int(input())):
    input()
    r,c = map(int,input().split())
    li = [list(input()) for _ in range(r)]
    count = 0
    for i in range(r):
        for j in range(2,c):
            if li[i][j-2] + li[i][j-1] + li[i][j] == '>o<':
                count += 1
                li[i][j-2],li[i][j-1],li[i][j] = '.','.','.'


    for j in range(c):
        for i in range(2,r):
            if li[i-2][j] + li[i-1][j] + li[i][j] == 'vo^':
                count += 1
                li[i-2][j],li[i-1][j],li[i][j] = '.','.','.'
    print(count)
