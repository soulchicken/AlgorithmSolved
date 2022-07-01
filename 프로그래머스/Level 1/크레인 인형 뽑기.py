def solution(board, moves):
    stack = []
    answer = 0
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1]:
                stack.append(board[i][move - 1])
                board[i][move - 1] = 0
                break
        while len(stack) >= 2:
            if stack[-1] != stack[-2]:
                break
            stack.pop()
            stack.pop()
            answer += 2
    return answer