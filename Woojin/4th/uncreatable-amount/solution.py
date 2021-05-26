from itertools import combinations

def solution(coins):
    result = set()
    
    for i in range(1, len(coins)):
        for comb in combinations(coins, i):
            result.add(sum(comb))
    
    return min(set(range(1, max(result) + 1)) - result)

print(solution([3, 2, 1, 1, 9]))
print(solution([3, 5, 7]))