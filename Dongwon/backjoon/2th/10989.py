# # 1차시도 heap 이용

# import heapq
# import sys
# input = sys.stdin.readline

# n = int(input())
# result = []

# for _ in range(n):
#     heapq.heappush(result, int(input()))

# while len(result):
#     print(heapq.heappop(result))

import sys
input = sys.stdin.readline

n = int(input())
result = [0 for _ in range(10001)]

for _ in range(n):
    target = int(input())
    result[target] += 1

for item in range(10001):
    if result[item] !=0:
        for _ in range(result[item]):
            print(item)