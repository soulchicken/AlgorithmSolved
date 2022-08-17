n = int(input())
while 1:
    q = input()
    if q == '=':
        break
    m = int(input())
    if q == '+':
        n += m
    elif q == '/':
        n //= m
    elif q == '*':
        n *= m
    else:
        n -= m
print(n)
