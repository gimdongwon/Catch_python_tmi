from bisect import bisect_left, bisect_right


def solution(x, sorted_numbers):
    start = bisect_left(sorted_numbers, x)
    end = bisect_right(sorted_numbers, x)
    result = end - start
    if result == 0:
        return -1
    else:
        return result


print(solution(2, [1, 1, 2, 2, 2, 2, 3]))
