from itertools import accumulate

def solution(board, skill):
    result = 0
    graph = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]
    
    for item in skill:
        t,r1,c1,r2,c2,degree = item
        if t == 1:
            graph[r1][c1] -= degree
            graph[r1][c2+1] += degree
            graph[r2+1][c1] += degree
            graph[r2+1][c2+1] -= degree
        else:
            graph[r1][c1] += degree
            graph[r1][c2+1] -= degree
            graph[r2+1][c1] -= degree
            graph[r2+1][c2+1] += degree
    
    # y 축 누적합
    for y in range(len(graph[0])):
        temp = graph[0][y]
        for x in range(1, len(graph)):
            temp += graph[x][y]
            graph[x][y] = temp
    print(list(accumulate(graph)))
    
    # x 축 누적합
    for x in range(len(graph)):
        temp = graph[x][0]
        for y in range(1, len(graph[0])):
            temp += graph[x][y]
            graph[x][y] = temp
    
    # 값 합치기
    for x in range(len(board)):
        for y in range(len(board[0])):
            board[x][y] += graph[x][y]
        
    # 남은 성 찾기
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] > 0:
                result += 1
    return result