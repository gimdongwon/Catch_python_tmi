def solution(food_times, k):
    if sum(food_times) <= k :
        return -1
    q = 1
    food_times = list(enumerate(food_times))
    while q :
        q = k // len(food_times)
        r = k % len(food_times)
        food_times = [(i, j-q) for (i, j) in food_times]
        re_food_times = []
        minus_val = 0
        for index, val in food_times :
            if val <= 0 :
                minus_val-=val
            else :
                re_food_times.append((index, val))
        k = r + minus_val
        food_times = re_food_times
    if len(food_times) == 0 :
        return -1
    return food_times[k][0] + 1
