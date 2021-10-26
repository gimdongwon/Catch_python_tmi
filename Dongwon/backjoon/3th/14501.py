n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    time = arr[i][0] + i
    # 뒤에 날짜가 가능하면 최댓값 변경
    if time <= n:
        dp[i] = max(arr[i][1] + dp[time], max(dp))
    # 뒤에 날짜가 불가능하면 최댓값은 그대로 감.
    else:
        dp[i] = max(dp)
print(max(dp))