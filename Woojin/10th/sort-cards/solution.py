# --- 백준 스타일 ---

from heapq import heappop, heappush

N = int(input())
cards = []
answer = 0

for _ in range(N):
    heappush(cards, int(input()))
    
while len(cards) >= 2:
    a = heappop(cards)
    b = heappop(cards)
    heappush(cards, a + b)
    answer += a + b

print(answer)