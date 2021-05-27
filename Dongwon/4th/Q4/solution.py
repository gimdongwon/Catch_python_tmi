from itertools import combinations

def solution(N, coins):
    coins = list(map(int, coins.split(" ")))
    result = []
    for i in range(1, N+1):
        temp = list(combinations(coins, i))
        for j in temp:
            result.append(sum(j))
    result = set(result)
    for i in range(1, 1000001):
        if i not in result:
            print(i)
            break
        
def solution2(N, coins):
    coins = list(map(int, coins.split(" ")))
    coins.sort()
    result = 1
    for i in coins:
        if result < i:
            break
        result += i
    print(result)

solution2(5, "3 2 1 1 9")
solution2(3, "1 2 3")
solution2(4, "1 2 3 5")
