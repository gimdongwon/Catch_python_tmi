from collections import deque

def bfs(s:int, virus_list:list, test_tube:list) :
    d_row = [1, 0, -1, 0]
    d_col = [0, 1, 0, -1]

    q = deque()
    q.extend(virus_list)
    while q :
        virus, x, y, count = q.popleft()
        if count == s :
            break
        count += 1
        for i in range(4) :
            nx = x + d_row[i]
            ny = y + d_col[i]
            if nx >= 0 and nx < len(test_tube) and ny >= 0 and ny < len(test_tube) and test_tube[nx][ny] == 0  :
                test_tube[nx][ny] = virus
                q.append([virus, nx, ny, count])
    return test_tube

def solution(n:int, k:int, test_tube:str, s:int, x:int, y:int)->int :

    test_tube = [[int(j) for j in test_tube[i:i + n]] for i in range(0, len(test_tube), n)]
    virus_list = []
    for i in range(n) :
        for j in range(n) :
            for virus in range(1, k+1) :
                if test_tube[i][j] == virus :
                    virus_list.append([virus, i, j, 0])
    test_tube = bfs(s, virus_list, test_tube)
    if test_tube[x-1][y-1] > 0 :
        return test_tube[x-1][y-1]
    else :
        return 0

print(solution(3,3,'102000300', 2,3,2))
print(solution(3,3,'102000300', 1,2,2))
    

    

