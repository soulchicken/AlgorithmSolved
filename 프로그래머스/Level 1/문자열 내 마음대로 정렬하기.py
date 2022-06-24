def solution(strings, n):
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings.sort()
    for i in range(len(strings)):
        strings[i] = strings[i][1:]
    return strings
