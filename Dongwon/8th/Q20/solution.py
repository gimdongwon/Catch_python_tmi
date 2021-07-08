from itertools import combinations
import copy

N = int(input())

graph =[]

for __ in range(N):
    graph.append(input().split())

Teachers = []
wall_candidates = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == "X":
            wall_candidates.append([i,j])
        elif graph[i][j] == "T":
            Teachers.append([i,j])

candidates = list(combinations(wall_candidates, 3))

def set_wall(candidates):
    for candidate in candidates:
        copy_graph = copy.deepcopy(graph)
        for i in range(3):
            copy_graph[candidate[i][0]][candidate[i][1]] = "O"
        if check_supervise(copy_graph, Teachers) == True:
            return "YES"
    return "NO"

def check_supervise(graphs, teachers):
    global N
    for teacher in teachers:
        x,y = teacher
        nx, ny = x, y
        # x 감소
        while nx > 0:
            nx -= 1
            if graphs[nx][ny] == "S":
                return False
            elif graphs[nx][ny] == "O":
                break
        nx, ny = x, y
        # x 증가
        while nx < N-1:
            nx += 1
            if graphs[nx][ny] == "S":
                return False
            elif graphs[nx][ny] == "O":
                break
        nx, ny = x, y
        # y 감소
        while ny > 0:
            ny -= 1
            if graphs[nx][ny] == "S":
                return False
            elif graphs[nx][ny] == "O":
                break
        nx, ny = x, y
        # y 증가
        while ny < N-1:
            ny += 1
            if graphs[nx][ny] == "S":
                return False
            elif graphs[nx][ny] == "O":
                break
    return True
result = set_wall(candidates)
print(result)