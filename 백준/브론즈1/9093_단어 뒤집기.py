for _ in range(int(input())):
    speak = list(input().split())
    for word in speak:
        print(word[::-1], end=' ')
    print()
