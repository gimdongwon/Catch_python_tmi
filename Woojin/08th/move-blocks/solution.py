# --- 모범 답안 ---

from collections import deque

# 시계방향
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 현재 위치에서 이동 가능한 위치 좌표를 반환
def get_possible_pos(pos, board):
    possible_pos = []    
    pos = list(pos) # 언팩하기 위해 리스트로 형변환
    x1, y1 = pos[0]
    x2, y2 = pos[1]
    
    # 시계방향 움직임
    for dx, dy in dirs:
        px1 = x1 + dx
        py1 = y1 + dy
        px2 = x2 + dx
        py2 = y2 + dy
        
        if board[px1][py1] == 0 and board[px2][py2] == 0:
            possible_pos.append({(px1, py1), (px2, py2)})
    
    # 회전방향 움직임
    if x1 == x2: # 가로위치에 있을때
        for i in [-1, 1]: # 위로회전, 아래로회전
            if board[x1 + i][y1] == 0 and board[x2 + i][y2] == 0:
                possible_pos.append({(x1, y1), (x1 + i, y1)})
                possible_pos.append({(x2, y2), (x2 + i, y2)})
    elif y1 == y2: # 세로위치에 있을 때
        for i in [-1, 1]: # 왼쪽회전, 오른쪽 회전
            if board[x1][y1 + i] == 0 and board[x2][y2 + i] == 0:
                possible_pos.append({(x1, y1), (x1, y1 + i)})
                possible_pos.append({(x2, y2), (x2, y2 + i)})
                
    return possible_pos

"""
위치이동 문제에서 보면 대부분 주어진 범위를 넘어가는 부분을
걸러줘야한다. 이런 경우 코드가 약간 길어지는데
이걸 막기위해서 주어진 보드의 4면에 1줄씩
벽을 세워주면 코드 길이를 줄일 수 있다.
"""
def solution(board):
    n = len(board)
    """
    방문리스트가 필요한 이유는 최단 거리 이후에도 방문하는 경우가 있음
    중복된 노드를 탐색하지 않기 위해서 방문 일지가 필요함
    """
    visited = [] # 방문리스트
    new_board = [[1] * (n + 2) for _ in range(n + 2)] # 4면을 벽으로 추가한 보드

    # 보드 옮기기
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            new_board[i][j] = board[i - 1][j - 1]

    # 로봇의 현재 위치
    pos = {(1, 1), (1, 2)}
    visited.append(pos)

    # 큐에 위치와 시간 삽입
    queue = deque()
    queue.append((pos, 0))
    
    # bfs로 최단 경로 탐색
    while queue:
        pos, cnt = queue.popleft()
        
        if (n, n) in pos:
            return cnt
        
        for possible_pos in get_possible_pos(pos, new_board):
            # 방문한 적이 없다면
            if possible_pos not in visited:
                # 방문처리와 큐 삽입
                visited.append(possible_pos)
                queue.append((possible_pos, cnt + 1))