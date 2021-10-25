# 1차 시도

import copy

n,m = map(int, input().split())

board = [list(input()) for _ in range(n)]
start = None
min_answer = 10000


for x in range(n-7):
    for y in range(m-7):
        result = 0
        graph = copy.deepcopy(board)
        for i in range(x,8+x):
            for j in range(y, y+8):
                if i == x and j == y:
                    start = graph[i][j]
                elif j == y and i > x:
                    if graph[i][j] == graph[i-1][j]:
                        result += 1
                        graph[i][j] = "B" if graph[i-1][j] == "W" else "W"
                else:
                    if graph[i][j] == graph[i][j-1]:
                        result += 1
                        graph[i][j] = "B" if graph[i][j-1] == "W" else "W"
        min_answer = min(result, min_answer)

print(min_answer)

# 2차 시도

import copy

n,m = map(int, input().split())

board = [list(input()) for _ in range(n)]
board = [
    list('BBBBBBBBBBBBBBBBBBBBBBB'), 
    list('BBBBBBBBBBBBBBBBBBBBBBB'),
    list('BBBBBBBBBBBBBBBBBBBBBBB'),
    list('BBBBBBBBBBBBBBBBBBBBBBB'),
    list('BBBBBBBBBBBBBBBBBBBBBBB'),
    list('BBBBBBBBBBBBBBBBBBBBBBB'),
    list('BBBBBBBBBBBBBBBBBBBBBBB'),
    list('BBBBBBBBBBBBBBBBBBBBBBB'),
    list('BBBBBBBBBBBBBBBBBBBBBBW')
    ]
start = None
min_answer = 10000


for x in range(n-7):
    for y in range(m-7):
        result = 0
        cnt_W, cnt_B = 0,0
        for i in range(x,8+x):
            for j in range(y, y+8):
                if (i + j) % 2 ==0:
                    if board[i][j] != "W":
                        cnt_W += 1
                    if board[i][j] != "B":
                        cnt_B += 1
                else:
                    if board[i][j] != "B":
                        cnt_W += 1
                    if board[i][j] != "W":
                        cnt_B += 1
        min_answer = min(cnt_B, cnt_W, min_answer)

print(min_answer)