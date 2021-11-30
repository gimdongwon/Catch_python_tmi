# # n = int(input())
# n = 6

# # stair = [int(input()) for _ in range(n)]
# stair = [10,20,15,25,10,20]

# dp = [0] * n
# dp[0] = stair[0]
# dp[1] = max(stair[1] + dp[0], stair[1])
# dp[2] = max(dp[0] + stair[2], stair[1] + stair[2])
# i = 3

# for i in range(3, n):
#     dp[i] = max(stair[i] + stair[i-1] + dp[i-3], dp[i-2] + stair[i])
#     i += 1

# print(max(dp))
import sys
input = sys.stdin.readline

n = int(input())
stair = [0 for _ in range(301)]
dp = [0 for _ in range(301)]

for i in range(n):
    stair[i] = int(input())

dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[0] + stair[1], stair[0] + stair[2])

for i in range(3, n):
    dp[i] = max(stair[i] + stair[i-1] + dp[i-3], dp[i-2] + stair[i])

print(dp[n-1])