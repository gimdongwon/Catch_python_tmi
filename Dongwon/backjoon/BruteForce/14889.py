# # 1차시도 실패

# from itertools import combinations

# n = int(input())

# board = [list(map(int, input().split())) for _ in range(n)]
# # board = [[0, 1, 2, 3],[4,0,5,6],[7,1,0,2],[3,4,5,0]]
# # board = [[0, 1, 2, 3, 4, 5], [1, 0, 2, 3, 4, 5] ,[1, 2, 0, 3, 4, 5] ,[1, 2, 3, 0, 4, 5] ,[1, 2, 3, 4, 0, 5] ,[1, 2, 3, 4, 5, 0]]

# members = [{item: 0} for item in range(n)]
# result = 100000
# used = []

# def set_team():
#     global result
#     start_team, link_team = [], []
#     for i in range(n):
#         if members[i][i] == 0:
#             start_team.append(i)
#         else:
#             link_team.append(i)
    
#     start_candiate = list(combinations(start_team, 2))
#     link_candiate = list(combinations(link_team, 2))
    
#     start_result = 0
#     link_result = 0
#     # print(start_candiate, link_candiate)
#     for i in range(len(start_candiate)):
#         start_result += board[start_candiate[i][0]][start_candiate[i][1]] + board[start_candiate[i][1]][start_candiate[i][0]]
#         link_result += board[link_candiate[i][0]][link_candiate[i][1]] + board[link_candiate[i][1]][link_candiate[i][0]]
#         # print(result,board[start_candiate[i][0]][start_candiate[i][1]] - board[link_candiate[i][0]][link_candiate[i][1]])
#     result = min(result, abs(start_result-link_result))

# def make_teams(member_cnt):
#     if member_cnt == n // 2 and str(members) not in used:
#         used.append(str(members))
#         set_team()
#         return
#     temp = 0
#     for i in range(n):
#         if members[i][i] == 0:
#             members[i][i] = 1
#             temp = 0
#             for j in range(n):
#                 temp += members[j][j]
#             make_teams(temp)
#             members[i][i] = 0

# make_teams(0)
# print(result)

# # 2차시도

from itertools import combinations

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
# board = [[0, 1, 2, 3],[4,0,5,6],[7,1,0,2],[3,4,5,0]]
members = [i for i in range(n)]

team_candidates = []
result = 10000

for team in list(combinations(members, n // 2)):
    team_candidates.append(team)

for i in range(len(team_candidates)//2):
    team = team_candidates[i]
    start_team_cnt = 0
    for j in range(n//2):
        member = team[j]
        for k in team:
            start_team_cnt += board[member][k]
    team = team_candidates[-i-1]
    link_team_cnt = 0
    for j in range(n//2):
        member = team[j]
        for k in team:
            link_team_cnt += board[member][k]
    result = min(result, abs(start_team_cnt - link_team_cnt))

print(result)