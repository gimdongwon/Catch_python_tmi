from collections import deque

def move_robot(position:list, board:list) -> list:
    d_row = [1, 0, -1, 0]
    d_col = [0, 1, 0, -1]
    y1, x1 = position[0]
    y2, x2 = position[1]
    move_position = []

    # 상하좌우
    for i in range(4) :
        if board[y1 + d_col[i]][x1 + d_row[i]] == 0 and board[y2 + d_col[i]][x2 + d_row[i]] == 0 :
            move_position.append({(y1 + d_col[i], x1 + d_row[i]), (y2 + d_col[i], x2 + d_row[i])})

    # 세로 -> 가로 
    if y1 == y2 :
        for i in range(1, 4, 2) :
            if board[y1 + d_col[i]][x1 + d_row[i]] == 0 and board[y2 + d_col[i]][x2 + d_row[i]] == 0 :
                move_position.append({(y1, x1), (y1 + d_col[i], x1)})
                move_position.append({(y2, x2), (y2 + d_col[i], x2)})
    # 가로 -> 세로
    else :
        for i in range(0, 4, 2) :
            if board[y1 + d_col[i]][x1 + d_row[i]] == 0 and board[y2 + d_col[i]][x2 + d_row[i]] == 0 :
                move_position.append({(y1, x1), (y1, x1 + d_row[i])})
                move_position.append({(y2, x2), (y2, x1 + d_row[i])})

    return move_position
    
def solution(board:list) :
    n = len(board)
    board = [[1] + b + [1] for b in board]
    board = [[1] * (n + 2)] + board + [[1] * (n + 2)]
    pos = {(1,1), (1,2)}
    q = deque()
    q.append([pos, 0])
    visited = []
    visited.append(pos)
    while q :
        pos, distance = q.popleft()
        distance += 1
        for position in move_robot(list(pos), board) :
            if (n, n) in position :
                return distance
            if position not in visited :
                q.append([position, distance])
                visited.append(position)
    return -1


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
