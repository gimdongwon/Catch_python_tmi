import heapq
board = [[],[],[],[]]
result = 0
answer = []

for j in range(4):
    temp = list(map(int, input().split()))
    for i in range(0, 8, 2):
        board[j].append((temp[i], temp[i+1]))

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

result = board[0][0][1]
board[0][0] = (0, board[0][0][1])

# 물고기 이동
def move_fish(shark_x, shark_y, graph):
    for i in range(1, 17):
        for x in range(4):
            flag = True
            for y in range(4):
                if graph[x][y][0] == i:
                    for k in range(8):
                        nx = dx[(k+graph[x][y][1]) % 8] + x
                        ny = dy[(k+graph[x][y][1]) % 8] + y
                        if -1 < nx < 4 and -1 < ny < 4 and graph[nx][ny] != 0:
                            graph[nx][ny], graph[x][y] = graph[x][y], graph[nx][ny]
                        # else:
                        #     # 방향 돌려야 함.
                        #     graph[x][y][1] = (graph[x][y][1] + 1) % 8
                    flag = False
                    break
            if flag == False:
                break
    move_shark(graph)

def move_shark(graph):
    global result
    flag = False
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == 0:
                nx = dx[graph[i][j][1]]
                ny = dy[graph[i][j][1]]
                
                for k in range(1,4):
                    if -1 < i + nx * k < 4 and -1 < j + ny * k < 4:
                        move_fish(i+nx*k, j+ny*k, graph)
                        graph[i][j] = (0, 0)
                        result += graph[i + nx * k][j + ny * k][0]
                        flag = True
                
                if nx > 4 or nx < 0 or ny > 4 or ny < 0:
                    answer.append(result)
                    result = board[0][0][1]
        if flag:
            break

move_fish(0,0, board)

print(answer)
