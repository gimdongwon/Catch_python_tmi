from collections import deque


def bfs(x: int, y: int, n: int, l: int, r: int, union: list, population: list):
    d_row = [1, 0, -1, 0]
    d_col = [0, 1, 0, -1]
    # 연합국가 리스트
    united = []
    united.append((x, y))
    q = deque()
    q.append((x, y))
    # 연합국가 표시
    union[x][y] = 1
    # 연합국 전체 인구수
    union_population = population[x][y]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + d_row[i]
            ny = y + d_col[i]
            if (
                nx >= 0
                and nx < n
                and ny >= 0
                and ny < n
                and union[nx][ny] == 0
                and abs(population[x][y] - population[nx][ny]) >= l
                and abs(population[x][y] - population[nx][ny]) <= r
            ):
                q.append((nx, ny))
                united.append((nx, ny))
                union[nx][ny] = 1
                union_population += population[nx][ny]
    # 인구수 조정
    for x_ind, y_ind in united:
        population[x_ind][y_ind] = union_population // len(united)
    return union, population


def solution(n: int, l: int, r: int, population: str):
    population = population.split()
    population = [[int(j) for j in population[i : i + n]] for i in range(0, n * n, n)]

    answer = 0

    while True:
        union = [[0] * n for _ in range(n)]
        break_count = 0
        for i in range(n):
            for j in range(n):
                if union[i][j] == 0:
                    union, population = bfs(i, j, n, l, r, union, population)
                    break_count += 1
        if break_count == n * n:
            break
        answer += 1

    return answer


print(solution(2, 20, 50, "50 30 20 40"))
print(solution(2, 40, 50, "50 30 20 40"))
print(solution(2, 20, 50, "50 30 30 40"))
print(solution(3, 5, 10, "10 15 20 20 30 25 40 22 10"))
print(solution(4, 10, 50, "10 100 20 90 80 100 60 70 70 20 30 40 50 20 100 10"))
