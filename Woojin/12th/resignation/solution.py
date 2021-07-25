# --- 백준 스타일 ---

N = int(input())
consults = []

for _ in range(N):
    consults.append(tuple(map(int, input().split())))

dp = [0] * (N + 1)
max_price = 0

for i in reversed(range(N)):
    time, price = consults[i]

    try:
        dp[i] = max(price + dp[i + time], max_price)
        max_price = dp[i]
    except IndexError:
        dp[i] = max_price
    
print(dp[0])