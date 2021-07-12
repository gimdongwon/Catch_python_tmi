from collections import defaultdict
import operator


def solution(n, stages):
    result = defaultdict(int)

    for i in range(1, n+1):
        players = 0
        for j in stages:
            if j >= i:
                players += 1
        result[i] = stages.count(i)/float(players)

    a = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
    return [x[0] for x in a]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))