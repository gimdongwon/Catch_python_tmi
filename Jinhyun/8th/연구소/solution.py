from itertools import combinations as cb
from collections import deque
from copy import deepcopy


def count_zero(lab: list) -> int:
    """
    바이러스가 다 퍼진 후 안전구역을 구하기 위한 함수
    """
    count = 0
    for i in lab:
        count += i.count(0)
    return count


def blank_virus(lab: list):
    """
    blank : 빈칸을 나타내는 0
    virus : 바이러스를 나타내는 2
    blank_virus : 빈칸과 바이러스의 좌표 따로 뽑아내는 작업
    """
    blank, virus = [], []
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if lab[i][j] == 0:
                blank.append((i, j))
            elif lab[i][j] == 2:
                virus.append((i, j))
    return blank, virus


def bfs(start: list, build_wall: tuple, lab: list):
    d_row = [1, 0, -1, 0]
    d_col = [0, 1, 0, -1]

    lab = deepcopy(lab)  # 기존의 lab은 보존해야 하기 때문에 deepcopy 사용
    for x, y in build_wall:
        lab[x][y] = 1

    q = deque()
    q.extend(start)  # virus 먼저 추가
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + d_row[i]
            ny = y + d_col[i]
            if (
                nx >= 0
                and nx < len(lab)
                and ny >= 0
                and ny < len(lab[0])
                and lab[nx][ny] == 0
            ):
                lab[nx][ny] = 2
                q.append((nx, ny))
    return count_zero(lab)


def solution(n: int, m: int, lab: str) -> int:

    lab_len = len(lab)
    lab = [[int(j) for j in lab[i : i + m]] for i in range(0, lab_len, m)]

    blank, virus = blank_virus(lab)
    build_wall = list(cb(blank, 3))

    answer = 0
    for build in build_wall:
        result = bfs(virus, build, lab)
        if answer < result:
            answer = result

    return answer


print(solution(7,7,"2000110001012001101000100000000001101000000100000"))
print(solution(4,6,"000000100002111002000002"))
print(solution(8, 8, "2000000220000002200000022000000220000002000000000000000000000000"))
