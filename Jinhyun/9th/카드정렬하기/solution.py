import heapq

def solution(n, card) :
    if n == 1 :
        return 0
    heapq.heapify(card)
    answer = 0
    while len(card) > 1 :
        first = heapq.heappop(card)
        second = heapq.heappop(card)
        answer += (first + second)
        heapq.heappush(card, first + second)
    return answer
    
print(solution(3, [10, 20, 40]))