N = int(input())
counts = [float('inf')]*(N+1)
stack = []

max_num = int(N**0.5)
stack.append((0,0))
max_count = float('inf')
while stack:
    count, index = stack.pop()
    if index <= N and max_count > count and counts[index] > count:
        counts[index] = count
        if index == N:
            counts[N] = count
        for i in range(1,max_num+1):
            stack.append((count+1,index + i**2))
print(counts[N])
