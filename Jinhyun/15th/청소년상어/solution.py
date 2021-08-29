from copy import deepcopy
import sys
from pprint import pprint

def dfs (f_x, f_y, eat, space, dic) :
    global answer

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]

    eat += space[f_x][f_y]
    space[f_x][f_y] = 0

    for fish_num in range(1, 17) :
        loc = None
        for i in range(4) :
            for j in range(4) :
                if space[i][j] == fish_num :
                    loc = (i, j)
        if loc is None :
            continue

        x, y = loc
        fish = dic[x][y]

        # 물고기의 이동
        for i in range(8) :
            nd = (fish + 1) % 8
            nx = x + dx[nd]
            ny = y + dy[nd]
            # 상어 위치 바꾸면 안되고 / 자기 벗어나는 경우 경로 바꿔주는 행동
            if not (nx >= 0 and nx < 4 and ny >= 0 and ny < 4) or ((nx, ny) == (f_x, f_y)):
                continue
            dic[x][y] = nd
            space[x][y], space[nx][ny] = space[nx][ny], space[x][y]
            dic[x][y], dic[nx][ny] = dic[nx][ny], dic[x][y]
            break

    answer = max(answer, eat)
    # 상어의 이동
    shark = dic[f_x][f_y]
    pprint(space)
    print('-' * 50)
    for i in range(1, 4) :
        n_x = f_x + dx[shark] * i 
        n_y = f_y + dy[shark] * i
        if n_x >= 0 and n_x < 4 and n_y >= 0 and n_y < 4 and space[n_x][n_y] > 0:
            dfs(n_x, n_y, eat, deepcopy(space), deepcopy(dic))

def solution(spaces) :
    dic = []
    space = []
    dic_tmp = []
    space_tmp = []
    for index, s in enumerate(spaces.split()) :    
        if index % 2 == 0 :
            space_tmp.append(int(s))
        else :
            dic_tmp.append(int(s) - 1)
        if len(dic_tmp) == 4 :
            dic.append(dic_tmp)
            dic_tmp = []
        if len(space_tmp) == 4 :
            space.append(space_tmp)
            space_tmp =[]

    dfs(0, 0, 0, space, dic)
    return answer

answer = 0
sys.setrecursionlimit(20000)
print(solution('7 6 2 3 15 6 9 8 3 1 1 8 14 7 10 1 6 1 13 6 4 3 11 4 16 1 8 7 5 2 12 2'))