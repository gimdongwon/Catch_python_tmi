from itertools import combinations as cb


def location(hallway: list, value: str) -> list:
    location = []
    hallway_len = len(hallway)
    for row in range(hallway_len):
        for col in range(hallway_len):
            if hallway[row][col] == value:
                location.append((row, col))
    return location


def dfs(teacher: list, obstacles: tuple, hallway: list) -> bool:
    d_row = [1, 0, -1, 0]
    d_col = [0, 1, 0, -1]

    # 장애물 설치
    for x, y in obstacles:
        hallway[x][y] = "O"

    for t_loc in teacher:
        x, y = t_loc
        for i in range(4):
            nx, ny = x, y
            while True:
                nx = nx + d_row[i]
                ny = ny + d_col[i]
                if not (
                    nx >= 0 and nx < len(hallway) and ny >= 0 and ny < len(hallway)
                ):
                    break
                if hallway[nx][ny] == "S":
                    return False
                if hallway[nx][ny] == "O":
                    break
    return True


def solution(n: int, hallway: str) -> str:
    hallway_len = len(hallway)
    hallway = [[j for j in hallway[i : i + n]] for i in range(0, hallway_len, n)]

    teacher = location(hallway, "T")
    blank = location(hallway, "X")

    obstacles = list(cb(blank, 3))
    for obstacle in obstacles:
        dfs(teacher, obstacle, hallway)
        if dfs(teacher, obstacle, hallway):
            return "YES"
    return "NO"


print(solution(5, "XSXXTTXSXXXXXXXXTXXXXXTXX"))
print(solution(4, "SSSTXXXXXXXXTTTX"))
