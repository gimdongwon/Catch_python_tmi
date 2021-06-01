# coding=utf-8
from itertools import combinations


def coin(items):
    a = []
    amount = []
    for i in range(1, len(items)+1):
        a.append(list(combinations(items, i)))
    for i in a:
        for j in i:
            amount.append(sum(j))
    amount.sort()

    for i in range(1, max(amount)):
        if i not in amount:
            return i


print(coin([3, 2, 1, 1, 9]))

