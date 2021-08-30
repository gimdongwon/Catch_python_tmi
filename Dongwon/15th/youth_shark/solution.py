import heapq
board = [[],[],[],[]]
result = 0

for j in range(4):
    temp = list(map(int, input().split()))
    for i in range(0, 8, 2):
        board[j].append((temp[i], temp[i+1]))

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

result += board[0][0][1]
board[0][0] = ("shark", board[0][0][1])

# 물고기 이동
def move_fish():
    for i in range(1, 17):
        for x in range(4):
            flag = True
            for y in range(4):
                if board[x][y][0] == i:
                    for k in range(8):
                        nx = dx[(k+board[x][y][1]) % 8] + x
                        ny = dy[(k+board[x][y][1]) % 8] + y
                        if -1 < nx < 4 and -1 < ny < 4 and board[nx][ny] != "shark":
                            board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
                        else:
                            # 방향 돌려야 함.
                            board[x][y][1] = (board[x][y][1] + 1) % 8
                    flag = False
                    break
            if flag == False:
                break
    move_shark()

def move_shark():
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == "shark":
                for k in range(8):
                    nx = dx[k] + board[i][j][1]
                    ny = dy[k] + board[i][j][1]
                    if -1 < nx < 4 and -1 < ny < 4:
                        # 여기를 모르겠다. ㅜㅜ
                        continue

move_fish()

print(board)
