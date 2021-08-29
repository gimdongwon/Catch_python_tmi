'''
bfs를 따라해보는 방법
어디서 조건이 틀렸는지는 파악을 못하고 있음
'''

def distance(x, y, nx, ny) :
    return abs(x - nx) + abs(y - ny)

def find_place(place) :
    place_list = []
    for i in range(5) :
        for j in range(5) :
            if place[i][j] == 'P' :
                place_list.append((i, j))
    return place_list


def search(candidates, place) :
    
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    
    if len(candidates) == 0 :
        return 1
    
    for candidate in candidates :
        x, y = candidate
        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < 5 and ny >= 0 and ny < 5 :
                if distance(x, y, nx, ny) == 1 :
                    if place[nx][ny] == 'P' :
                        return 0
                else :
                    if place[nx][ny] == 'P' :
                        if place[x][ny] != 'X' or place[nx][y] != 'X' :
                            return 0
        for j in range(0, 8, 2) :
            nx = x + 2 * dx[j]
            ny = y + 2 * dy[j]
            if nx >= 0 and nx < 5 and ny >= 0 and ny < 5 :
                c_x = (x + nx) // 2
                c_y = (y + ny) // 2
                if place[nx][ny] == 'P' and place[c_x][c_y] != 'X' :
                    return 0
        return 1
    

def solution(places):
    answer = []
    for place in places :
        candidates = find_place(place)
        pf = search(candidates, place)
        answer.append(pf)
    return answer