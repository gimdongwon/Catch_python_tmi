n = int(input())

board = [list(map(int, input().split())) for i in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            pre_left = 0
        else:
            pre_left = board[i-1][j-1]
        if j == i:
            pre_right = 0
        else:
            pre_right = board[i-1][j]

        board[i][j] = board[i][j] + max(pre_left, pre_right)

# result = 0

print(max(board[n-1]))