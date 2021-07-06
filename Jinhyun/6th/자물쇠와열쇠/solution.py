def rotation_90(key:list) -> list :
    '''
    key = [[1,2,3],[4,5,6],[7,8,9]]
    *key = [1,2,3],[4,5,6],[7,8,9]
    zip(*key) -> (1,4,7), (2,5,8) (3,6,9)
    reversed -> (7,4,1), (8,5,2), (9,6,3)
    '''
    return [list(reversed(i)) for i in zip(*key)]

def check_all_one_lock (new_lock:list) -> bool :
    '''
    상하좌우 3배 키운 자물쇠
    '''
    lock_len = len(new_lock) // 3
    for i in range(lock_len, lock_len * 2) :
        for j in range(lock_len, lock_len * 2) :
            if new_lock[i][j] != 1 :
                return False
    return True

def solution(key:list, lock:list) -> bool :
    m = len(key)
    n = len(lock)

    # 상하좌우 3배 키운 자물쇠
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 기존 자물쇠의 센터에 값 할당
    for i in range(n) :
        for j in range(n) :
            new_lock[i + n][j + n] = lock[i][j]
    for _ in range(4) :
        key = rotation_90(key)
        # n-m 을 해도 되는 이유 : 중앙 자물쇠 직전부터 시작하기 위해서
        # n-m+1(겹쳐서 시작)도 생각했는데 자물쇠가 다 1인 경우에는 오류가 날 수도 있다고 생각했음
        for x in range(n - m, n * 2) :
            for y in range(n - m, n * 2) :
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x + i][y + j] += key[i][j]
                if check_all_one_lock(new_lock) :
                    return True
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x + i][y + j] -= key[i][j]
    return False


print(solution([[0,0,0],[1,0,0],[0,1,1]],[[1,1,1],[1,1,0],[1,0,1]]))