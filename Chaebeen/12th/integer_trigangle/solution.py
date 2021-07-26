def solution(n, triangle):
    for i in range(1, n):
        for j in range(i + 1):
            # 왼쪽 대각선
            left = 0 if j == 0 else triangle[i - 1][j - 1]
            # 오른쪽 대각선
            right = 0 if j == i else triangle[i - 1][j]
            triangle[i][j] += max(left, right)

    return max(triangle[n - 1])  # 마지막 열에서 가장 큰 수


print solution(5, [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
