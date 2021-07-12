import numpy as np


def solution(homes):
    average = sum(homes) / float(len(homes))
    return homes[np.abs(np.array(homes) - average).argmin()]


print(solution([7, 5, 1, 7, 7, 9]))
