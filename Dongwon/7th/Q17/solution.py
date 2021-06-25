from collections import deque

def solution(X,Y, graph, last_position):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    que = []
    for i in range(X):
        for j in range(Y):
            if graph[i][j] != 0:
                que.append([graph[i][j], i,j,0])
    # 1,2,3 순서대로 감염시키기 위해 맨 앞에 값 삽입
    que.sort()
    que = deque(que)
    while que:
        z, x,y, time = que.popleft()
        if time == last_position[0]:
            break
        p = graph[x][y]
        for i in range(4):
            new_x = dx[i] + x
            new_y = dy[i] + y
            if -1 < new_x < Y and -1 < new_y < Y and graph[new_x][new_y] == 0:
                graph[new_x][new_y] = p
                que.append([graph[new_x][new_y], new_x,new_y, time+1])
                
    print(graph[last_position[1]-1][last_position[2]-1])

solution(3,3,[[1,0,2],[0,0,0],[3,0,0]], [2,3,2])
solution(3,3,[[1,0,2],[0,0,0],[3,0,0]], [1,2,2])