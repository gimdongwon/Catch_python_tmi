def solution(N,M,board):
    # N, M = map(int, input().split())

    # board = []

    # for i in range(N):
    #     board.append(list(map(int, input().split())))

    visited = set([])

    chicken = []
    house = []
    result = 0
    answer = 0
    sums = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 2:
                chicken.append([i,j])
            elif board[i][j] == 1:
                house.append([i,j])

    for item in house:
        temp = []
        for jtem in chicken:
            temp.append(abs(item[0] - jtem[0]) + abs(item[1] - jtem[1]))
        result += min(temp)
        visited.add(temp.index(min(temp)))
        # print(temp, visited, sum(temp))
        sums.append(sum(temp))
        answer = result if len(visited)<=M else min(sums)
    print(answer)

solution(5,3,[[0,0,1,0,0], [0,0,2,0,1],[0,1,2,0,0],[0,0,1,0,0],[0,0,0,0,2]])
solution(5,2,[[0,2,0,1,0], [1,0,1,0,0],[0,0,0,0,0],[2,0,0,1,1],[2,2,0,1,2]])
solution(5,1,[[1,2,0,0,0], [1,2,0,0,0],[1,2,0,0,0],[1,2,0,0,0],[1,2,0,0,0]])
solution(5,1,[[1,2,0,2,1], [1,2,0,2,1],[1,2,0,2,1],[1,2,0,2,1],[1,2,0,2,1]])