'''
응시자의 좌표를 구한 후 모든 경우의수를 따지는 방법
5 * 5 라서 가능한 방법
'''

from itertools import combinations

def distance(x, y, nx, ny) :
    return abs(x - nx) + abs(y - ny)

def find_place(place) :
    place_list = []
    for i in range(5) :
        for j in range(5) :
            if place[i][j] == 'P' :
                place_list.append((i, j))
    return place_list

def solution(places) :
    answer = [1] * len(places)
    for ind, place in enumerate(places) :
        candidates = find_place(place)
        for i in combinations(candidates, 2) :
            x = i[0]
            y = i[1]
            if distance(x[0], x[1], y[0], y[1]) == 1 :
                answer[ind] = 0
                break
            elif distance(x[0], x[1], y[0], y[1]) == 2 :
                if abs(x[0] - y[0]) == 2 or abs(x[1] - y[1]) == 2 :
                    c_x = (x[0] + y[0]) // 2
                    c_y = (x[1] + y[1]) // 2
                    if place[c_x][c_y] != 'X' :
                        answer[ind] = 0
                        break
                else :
                    if place[x[0]][y[1]] != 'X' or place[y[0]][x[1]] != 'X' :
                        answer[ind] = 0
                        break
    return answer