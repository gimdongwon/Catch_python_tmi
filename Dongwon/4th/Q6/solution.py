# 정확성 풀이 - 정확성 합

from collections import deque

def solution(food_times, k):
    time = 0
    que = deque([])
    for idx, item in enumerate(food_times):
            que.append((idx, item))
    while que and time < k:
        idx, item = que.popleft()
        if item - 1 > 0:
            que.append((idx, item-1))
        time += 1
        # print(que, time)
    if que:
        idx, item = que.popleft()
        return idx + 1
    else:
        return -1


# 그리디 접근 - 오답

def solution(food_times, k):
    result = k % len(food_times)
    # print(k // len(food_times), k % len(food_times))
    temp = list(map(lambda x: x - (k//len(food_times)), food_times))
    minus = sum(list(filter(lambda x: x < 0, temp)))
    # print(result, temp, minus)
    return minus + 1 if minus >=0 else abs(minus)
    
        
# 그리디 접근 - 정답

import heapq

def solution(food_times, k):
    que = []
    leng = len(food_times)
    for i in range(len(food_times)):
        heapq.heappush(que, (food_times[i], i+1))
    pre_food = 0
    min_food = que[0][0]
    
    while k - (min_food - pre_food) * leng >= 0:
        k -= (min_food - pre_food) * leng
        heapq.heappop(que)
        pre_food = min_food
        leng -= 1
        if not que:
            return -1
        min_food = que[0][0]
        
    idx = k % leng
    que.sort(key=lambda x: x[1])
    return que[idx][1]