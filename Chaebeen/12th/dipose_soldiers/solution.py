def solution(n, soldiers):
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if soldiers[i] < soldiers[j]:
                dp[i] = max(dp[j] + 1, dp[i])  # 감소하는 수열의 최대 길이
    print(dp)
    return n - max(dp)


print(solution(7, [15, 11, 4, 8, 5, 2, 4]))
