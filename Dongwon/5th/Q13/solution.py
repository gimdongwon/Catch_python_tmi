from itertools import combinations

def solution(N,M,board):
    # N, M = map(int, input().split())

    # board = []

    # for i in range(N):
    #     board.append(list(map(int, input().split())))

    # 삭제 가능한 치킨 집과 집으로 매칭하여 탐색

    chicken = []
    house = []
    sums = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 2:
                chicken.append([i,j])
            elif board[i][j] == 1:
                house.append([i,j])
    result = list(combinations(chicken, M))
    
    for resultItem in result:
        distance = 0
        for item in house:
            temp = []
            for jtem in resultItem:
                temp.append(abs(item[0] - jtem[0]) + abs(item[1] - jtem[1]))
            # 가장 최소 값만 합하기
            distance += min(temp)
        sums.append(distance)
    print(min(sums))

solution(5,3,[[0,0,1,0,0], [0,0,2,0,1],[0,1,2,0,0],[0,0,1,0,0],[0,0,0,0,2]])
solution(5,2,[[0,2,0,1,0], [1,0,1,0,0],[0,0,0,0,0],[2,0,0,1,1],[2,2,0,1,2]])
solution(5,1,[[1,2,0,0,0], [1,2,0,0,0],[1,2,0,0,0],[1,2,0,0,0],[1,2,0,0,0]])
solution(5,1,[[1,2,0,2,1], [1,2,0,2,1],[1,2,0,2,1],[1,2,0,2,1],[1,2,0,2,1]])
# solution()