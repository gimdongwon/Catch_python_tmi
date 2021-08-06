n,m = map(int, input().split())
# n,m = 4,4
b = list(map(int, input().split(" ")))
# b = "1 3 3 2 2 1 4 1 0 6 4 7"
board = [(b[i:i+m]) for i in range(0, len(b), m)]

# 두번째 열부터 고려
for j in range(1,m):
    for i in range(n):
        # 오른쪽 위
        if i == 0: # 예외처리 : 맨 위일때
            left_up = 0
        else:
            left_up = board[i-1][j-1]
        # 오른쪽 아래
        if i == n-1: # 예외처리 : 맨 아래일 때
            left_down = 0
        else:
            left_down = board[i+1][j-1]
        # 오른쪽
        left = board[i][j-1]
        
        board[i][j] = board[i][j] + max(left, left_down, left_up)
result = 0
print(board)
for i in range(n):
    result = max(result, board[i][m-1])
print(result)