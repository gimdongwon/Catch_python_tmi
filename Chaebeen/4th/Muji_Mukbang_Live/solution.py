# 정확성만 성공한 코드(효율성 실패)
def next_food(food_times, k):
    result = 0
    zero = []
    n = len(food_times)

    for i in range(n, n + max(food_times) * n):
        index = abs(n - i) % n
        if food_times[index] > 0:
            food_times[index] -= 1
            result += 1
            if result > k:
                return index + 1
            if food_times[index] == 0:
                zero.append(index)
                if len(set(zero)) == n:
                    return -1
    return -1


print(next_food([3, 2, 1], 5))