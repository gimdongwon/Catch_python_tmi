n = int(input())

consult = [list(map(int,input().split())) for _ in range(n)]

dp = [0] * (n + 1) # 0부터 세줌 +1 안하면 런타임 에러
max_value = 0

# 뒤에서 부터 최대 값 확인
for i in range(n-1, -1, -1):
    # i를 더해서 뒤에 남은 일수를 구해 가능한지 판단
    time = consult[i][0] + i
    if time <= n:
        # dp[i] = max(consult[i][1] + dp[time], max_value)
        # max_value = dp[i]
        dp[i] = max(consult[i][1] + dp[time], max(dp))
    else:
        # dp[i] = max_value
        dp[i] = max(dp)
    # print(consult[i][0], i, time, n, max_value, dp)
# print(max_value)
print(max(dp))