# 정확성 1개 실패, 효율성 전부 실패

from itertools import chain

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    while k:
        for i, f in enumerate(food_times):
            if k == 0:
                break
            
            if f > 0:
                food_times[i] -= 1
                k -= 1
    
    n = len(food_times)
    
    if i == n - 1:
        i = 0
    
    for j in chain(range(i, n), range(i)):
        if food_times[j] > 0:
            return j + 1
        
# 정확성 전부 성공, 효율성 전부 실패

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    food_times = list(enumerate(food_times))
    
    while k >= len(food_times):
        k -= len(food_times)
        food_times = [(f[0], f[1] - 1) for f in food_times if f[1] > 1]
        
    for i in range(len(food_times)):
        if k == 0 and food_times[i][1] > 0:
            return food_times[i][0] + 1
        
        if k > 0:
            food_times[i] = (food_times[i][0], food_times[i][1] - 1)
            k -= 1

# --- 정확성 및 효율성 성공 ---
# --- 아래 코드만 리뷰 부탁드립니다. ---

def solution(food_times, k):
    if sum(food_times) <= k: # -1 을 리턴하는 예외 케이스
        return -1
    
    food_times = list(enumerate(food_times))
    q = 1 # 아래의 while 문을 통과시키기 위해 q를 1로 초기화
    
    while q:
        q, r = divmod(k, len(food_times)) # q: 몫, r: 나머지
        food_times = list(map(lambda x: (x[0], x[1] - q), food_times))
        remainder_times = []
        
        for time in food_times:
            if time[1] > 0:
                remainder_times.append(time)
            else:
                r -= time[1]
        
        food_times = remainder_times
        k = r

    for time in food_times:
        if k == 0 and time[1] > 0:
            return time[0] + 1
        
        if k > 0:
            time = (time[0], time[1] - 1)
            k -= 1
            
print(solution([9, 3, 1, 2, 2, 3], 12))