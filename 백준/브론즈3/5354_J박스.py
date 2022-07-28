m = int(input())
for i in range(m):
    n = int(input())
    if n == 1:
        print('#')
    else:
        print('#'*n + '\n' + ('#' + 'J'*(n-2) + '#' + '\n')*(n-2)  + '#'*n)
    if i != m-1:
        print()
