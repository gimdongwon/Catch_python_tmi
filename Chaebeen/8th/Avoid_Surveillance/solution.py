# coding=utf-8
from itertools import combinations


def solution(n, board):
    students = []
    teachers = []
    spaces = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'S':
                students.append([i, j])
            elif board[i][j] == 'T':
                teachers.append([i, j])
            elif board[i][j] == 'X':
                spaces.append([i, j])

    for objects in combinations(spaces, 3):  # 장애물이 될 수 있는 모든 조합
        if check(students, teachers, objects, n):
            return True
    return False


def check(students, teachers, objects, n):
    # 상
    for x, y in students:
        while y >= 0:
            if [x, y] in objects:  # 장애물 만나면 건너뛰고
                break
            elif [x, y] in teachers:  # 선생님 만나면 False 리턴
                return False
            y -= 1
    # 하
    for x, y in students:
        while y < n:
            if [x, y] in objects:
                break
            elif [x, y] in teachers:
                return False
            y += 1
    # 좌
    for x, y in students:
        while x >= 0:
            if [x, y] in objects:
                break
            elif [x, y] in teachers:
                return False
            x -= 1
    # 우
    for x, y in students:
        while x < n:
            if [x, y] in objects:
                break
            elif [x, y] in teachers:
                return False
            x += 1
    return True  # 모두 통과혰을 경우 True 리턴


print(solution(5,
               [['X', 'S', 'X', 'X', 'T'],
                ['T', 'X', 'S', 'X', 'X'],
                ['X', 'X', 'X', 'X', 'X'],
                ['X', 'T', 'X', 'X', 'X'],
                ['X', 'X', 'T', 'X', 'X']])
      )
