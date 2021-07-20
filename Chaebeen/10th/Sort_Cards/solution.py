def solution(cards):
    cards.sort()
    result = 0
    for i in range(1, len(cards)):
        result += sum(cards[i:i+2])
        cards[i] = result
    return result


print(solution([10, 20, 40]))
