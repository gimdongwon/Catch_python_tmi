from collections import deque

def solution(board):
    N = len(board)
    # 첫 위치 초기화
    que = deque([(0, 0), (0, 1), 0])
    while que:
        cur_1, cur_2, time = que.popleft()
        if cur_1 == (N,N) or cur_2 == (N,N):
            return time
        # 이동하고 큐에 추가
        
    def move(current):
        # 평행 이동 가로
        # 평행 이동 세로

        # 가로 회전
        # 세로 회전
        pass