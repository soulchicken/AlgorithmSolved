n = int(input())
g, s, t = '@'*n, ' '*n, '\n'
print((g + s*3 + g + t)*2*n + (g*5+t)*n + (g + s*3 + g + t)*n + (g*5+t)*n)
