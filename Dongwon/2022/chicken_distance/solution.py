from itertools import combinations

def solution(n,m,board):
    # n,m = map(int, input())

    # board = []

    # for _ in range(n):
    #     board.append(list(map(int, input().split())))
    houses = []
    chicken_stores = []
    # result = int(1e9)
    result = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                houses.append([i,j])
            elif board[i][j] == 2:
                chicken_stores.append([i,j])
    
    for item in list(combinations(chicken_stores, m)):
        distance = 0
        for house in houses:
            x,y = house
            # min_value = 20000*m
            min_value = []
            for jtem in item:
                jx,jy = jtem
                min_value.append(abs(x-jx) + abs(y-jy))
                # min_value = min(min_value, abs(x-jx) + abs(y-jy))
            distance += min(min_value)
        # result = min(result, distance)
        result.append(distance)
    # print(min(result))
    print(result)


solution(5,3,[[0,0,1,0,0], [0,0,2,0,1], [0,1,2,0,0],[0,0,1,0,0], [0,0,0,0,2]]) # 5
solution(5,2,[[0,2,0,1,0], [1,0,1,0,0], [0,0,0,0,0],[2,0,0,1,1], [2,2,0,1,2]]) # 10
solution(5,1,[[1,2,0,0,0], [1,2,0,0,0], [1,2,0,0,0],[1,2,0,0,0], [1,2,0,0,0]]) # 11
solution(5,1,[[1,2,0,2,1], [1,2,0,2,1], [1,2,0,2,1],[1,2,0,2,1], [1,2,0,2,1]]) # 32