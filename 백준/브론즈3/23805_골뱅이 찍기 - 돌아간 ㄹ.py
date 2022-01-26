n = int(input())

g = '@' * n
s = ' ' * n
e = '\n'

alt1 = (g + s + g + s + g + e) * 3 * n
alt0 = (g * 3 + s + g + e) * n
alt2 = (g + s + g * 3 + e) * n

print(alt0+alt1+alt2)