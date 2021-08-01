'''
n(1-100)개의 도시
m(1-100,000)개의 버스
각 버스 한번 사용시 비용 있음
시작도시 도착도시 비용
'''
def solution(n, m, s_e_c) :
    # start, end, cost 인자 받기
    s_e_c = list(map(int, s_e_c.split()))
    s_e_c = [s_e_c[i:i+3] for i in range(0, len(s_e_c), 3)]
    # floyd 위한 데이터 대입
    INF = int(1e9)
    floyd = [[INF] * (n + 1) for _ in range(n+1)]
    for i in range(n + 1) :
        floyd[i][i] = 0

    for start, end, cost in s_e_c :
        # 최솟값만 저장
        if floyd[start][end] > cost :
            floyd[start][end] = cost

    # floyd
    for k in range(1, n + 1) :
        for a in range(1, n + 1) :
            for b in range(1, n + 1) :
                floyd[a][b] = min(floyd[a][b], floyd[a][k] + floyd[k][b])

    # 출력
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            if floyd[a][b] == INF :
                print("INF", end=" ")
            else :
                print(floyd[a][b], end = " ")
        print()

solution(5, 14, '1 2 2 1 3 3 1 4 1 1 5 10 2 4 2 3 4 1 3 5 1 4 5 3 3 5 10 3 1 8 1 4 2 5 1 7 3 4 2 5 2 4')