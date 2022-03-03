n = int(input())
li = [list(input().rstrip()) for _ in range(n)]

max_count = 1
for i in range(n-1):
    for j in range(n):
        li[i][j], li[i+1][j] = li[i+1][j], li[i][j]
        count = 1
        candy = ""
        for a in range(n):
            if candy != li[i+1][a]:
                max_count = max(count,max_count)
                count = 1
                candy = li[i+1][a]
            else:
                count += 1
        max_count = max(count,max_count)
        count = 1
        candy = ""
        for a in range(n):
            if candy != li[i][a]:
                max_count = max(count,max_count)
                count = 1
                candy = li[i][a]
            else:
                count += 1
        max_count = max(count,max_count)
        count = 1
        candy = ""
        for a in range(n):
            if candy != li[a][j]:
                max_count = max(count,max_count)
                count = 1
                candy = li[a][j]
            else:
                count += 1
        max_count = max(count,max_count)
        li[i][j], li[i+1][j] = li[i+1][j], li[i][j]
        


for i in range(n):
    for j in range(n-1):
        li[i][j], li[i][j+1] = li[i][j+1], li[i][j]
        count = 1
        candy = ""
        for a in range(n):
            if candy != li[a][j]:
                max_count = max(count,max_count)
                count = 1
                candy = li[a][j]
            else:
                count += 1
        
        max_count = max(count,max_count)

        count = 1
        candy = ""
        for a in range(n):
            if candy != li[i][a]:
                max_count = max(count,max_count)
                count = 1
                candy = li[i][a]
            else:
                count += 1
        max_count = max(count,max_count)

        count = 1
        candy = ""
        for a in range(n):
            if candy != li[a][j+1]:
                max_count = max(count,max_count)
                count = 1
                candy = li[a][j+1]
            else:
                count += 1
        max_count = max(count,max_count)

        li[i][j], li[i][j+1] = li[i][j+1], li[i][j]
        

print(max_count)
