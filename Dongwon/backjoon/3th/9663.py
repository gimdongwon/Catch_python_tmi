n = int(input())

board = [0 for _ in range(16)]
result = 0

def dfs(cnt):
    global result
    if cnt > n:
        result += 1
    else:
        for i in range(1, n+1):
            board[cnt] = i
            if isTrue(cnt):
                dfs(cnt+1)

def isTrue(x):
    for i in range(1, x):
        if board[x] == board[i] or abs(board[x] - board[i]) == x-i:
            return False
    return True

dfs(1)
print(result)