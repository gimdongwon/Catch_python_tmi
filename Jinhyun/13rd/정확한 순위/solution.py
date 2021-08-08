'''
시험을 본 학생 N명 성적 분실
학새 성적순위 정확하게 알 수 있는 학생은?
a, b -> a번 학생의 성적이 b번 학생보다 낮다
'''

from pprint import pprint

def solution(n, m, a, b) :
    INF = int(1e9)
    floyd = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1) :
        floyd[i][i] = 0
    
    for i in range(m) :
        floyd[a[i]][b[i]] = 1
    
    for k in range(1, n + 1) :
        for x in range(1, n + 1) :
            for y in range(1, n + 1) :
                floyd[x][y] = min(floyd[x][y], floyd[x][k]+floyd[k][y])
    
    result = 0
    for x_val in range(1, n+1) :
        count = 0
        for y_val in range(1, n+1) :
            if floyd[x_val][y_val] != INF or floyd[y_val][x_val] != INF :
                count += 1
        if count == n :
            result +=1
    
    return result

print(solution(6, 6, [1,3,4,4,5,5], [5,4,2,6,2,4]))
