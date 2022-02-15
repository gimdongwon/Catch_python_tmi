from copy import deepcopy
max_diff, max_board = 0, []

from itertools import combinations_with_replacement

def solution(n, info):
    result = [0 for _ in range(11)]
    max_num = 0
    win = False
    candidates = list(combinations_with_replacement(range(0,11), n))
    
    for candidate in candidates:
        temp = [0 for _ in range(11)]
        for item in candidate:
            temp[10-item] += 1
    
        ryan = 0
        apeach = 0
        
        for i, (r,a) in enumerate(zip(temp, info)):
            if r == a == 0:
                continue
            elif a >= r:
                apeach += (10 - i)
            else:
                ryan += (10 - i)
        
        if ryan > apeach:
            win = True
            if ryan - apeach > max_num:
                max_num = ryan-apeach
                result = temp
    
    return result if win else [-1]

def dfs_solution(n, info):
    def dfs(a_score, r_score, cnt, idx, board):
        global max_diff, max_board
        if cnt > n:
            return
        
        if idx > 10:
            diff = r_score - a_score
            if diff > max_diff:
                board[10] = n - cnt
                max_board = board
                max_diff = diff
            return
        if cnt < n:
            board2 = deepcopy(board)
            board2[10-idx] = info[10-idx] + 1
            dfs(a_score, r_score + idx, cnt + info[10-idx]+1, idx+1, board2)
        
        board1 = deepcopy(board)
    
        if info[10-idx] > 0:
            dfs(a_score+idx, r_score, cnt, idx+1, board1)
        else:
            dfs(a_score, r_score, cnt, idx+1, board1)
    
    dfs(0,0,0,0, [0]*11)
    
    return max_board if max_board else [-1]