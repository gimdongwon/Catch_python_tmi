def solution(n, m, golds):
    gold_map = [[0] * m for _ in range(n)]
    result = 0
    # 금광 지도 만들기
    for i in range(n):
        for j in range(m):
            gold_map[i][j] = golds[(i * m) + j]

    for j in range(1, m):
        for i in range(n):
            # 위
            up = 0 if i == 0 else gold_map[i - 1][j - 1]
            # 아래
            down = 0 if i == n - 1 else gold_map[i + 1][j - 1]
            # 옆
            side = gold_map[i][j - 1]
            print(up, down, side)
            gold_map[i][j] += max(up, down, side)

    for i in range(n):
        result = max(result, gold_map[i][m - 1])  # 마지막 열에서 가장 큰 수

    return result


print(solution(3, 4, [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7]))
