# --- 백준 스타일 ---

from heapq import heappop, heappush

N = int(input())
cards = []
answer = 0

for _ in range(N):
    heappush(cards, int(input()))
    
while len(cards) >= 2:
    min1 = heappop(cards)
    min2 = heappop(cards)
    heappush(cards, min1 + min2)
    answer += min1 + min2

print(answer)