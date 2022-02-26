n = int(input()) - 1
li = [1,2,4,7,8,11,13,14]
a = (n // 8)*15
b = li[n % 8]
print(a+b)