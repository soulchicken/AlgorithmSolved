s = input()
li = [s]
for i in range(len(s) - 2):
    for j in range(i+1,len(s) - 1):
        a = s[:i+1][::-1] + s[i+1:j+1][::-1] + s[j+1:][::-1]
        li.append(a)
li.sort()
print(li[0])
