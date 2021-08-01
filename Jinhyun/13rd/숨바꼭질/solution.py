def solution(n, m, barn_1, barn_2) :
    INF = int(1e9)
    hide = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1) :
        hide[i][i] = 0
    for j in range(m) :
        hide[barn_1[j]][barn_2[j]] = 1
        hide[barn_2[j]][barn_1[j]] = 1
    for k in range(1, n + 1) :
        for a in range(1, n + 1) :
            for b in range(1, n + 1) :
                hide[a][b] = min(hide[a][b], hide[a][k] + hide[k][b])

    dongbin_start = hide[1]
    dongbin_start[0] = -1
    max_val = max(dongbin_start)
    index = dongbin_start.index(max_val)
    count = dongbin_start.count(max_val)
    print(index, max_val, count)

solution(6, 7, [3,4,3,1,1,2,5],[6,3,2,3,2,4,2])