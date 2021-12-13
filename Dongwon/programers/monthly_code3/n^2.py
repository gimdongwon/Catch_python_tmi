# def solution(n, left, right):
#     board = [[0] * n for _ in range(n)]
    
#     for k in range(n):
#         for i in range(k+1):
#             for j in range(k+1):
#                 if board[i][j] == 0:
#                     board[i][j] = k+1
#     result = []
#     for item in board:
#         result.extend(item)
#     print(result) 
#     return result[left:right+1]

def solution(n,left, right):
    result = []
    
    for i in range(left, right+1):
        result.append(max(divmod(i,n)) + 1)
    return result