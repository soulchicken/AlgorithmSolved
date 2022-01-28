n = int(input())
g = '@'*n
s = ' '*n
e = '\n'
alt1 = (g + 3*s + g +e)*n
alt2 = (g + 2*s + g +e)*n
alt3 = (3 * g +e)*n
print(alt1+alt2+alt3+alt2+alt1)