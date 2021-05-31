# 풀이 1 (coins의 개수가 커질 수록 매우 비효율적일 듯)

from itertools import combinations

def solution(coins):
    result = set()
    
    for i in range(1, len(coins)):
        for comb in combinations(coins, i):
            result.add(sum(comb))

    return min(set(range(1, max(result) + 2)) - result)

# 풀이 2 (모든 금액들의 조합을 찾지 않고 만들 수 없는 금액을 찾는 풀이)

def solution(coins):
    coins.sort()
    
    if coins[0] > 1:
        return 1
    
    result = {coins[0]}
    
    for coin in coins[1:]:
        if coin > max(result) + 1:
            return max(result) + 1
        
        for r in set(result):
            result.add(r + coin)
        
        result.add(coin)

    return max(result) + 1
    

print(solution([3, 2, 1, 1, 9]))
print(solution([3, 5, 7]))
print(solution([1, 2, 2, 3]))