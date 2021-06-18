# 자물쇠 회전
def rotate(key):
    n = len(key)
    m = len(key[0])
    result = [[0]*n for __ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = key[i][j]
    return result

# 자물쇠와 열쇠가 맞는지 체크
def check(new_lock):
    lock_length = len(new_lock)//3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 회전했을 때 범위 벗어나는 경우 제외하기 위해 3배로 재설정
    new_lock = [[0]*n*3 for __ in range(n*3)]

    # 확대한 자물쇠에다 기존 자물쇠 중앙에 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for __ in range(4):
        # 회전
        key = rotate(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock)==True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))