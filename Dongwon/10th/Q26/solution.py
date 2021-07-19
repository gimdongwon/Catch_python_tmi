import heapq

N = int(input())

cards = [int(input()) for __ in range(N)]

heapq.heapify(cards)
answer = 0

while len(cards)>1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    answer += a+b
    heapq.heappush(cards, a+b)

print(answer)