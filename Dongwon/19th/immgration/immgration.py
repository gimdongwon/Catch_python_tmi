def solution(n, times):
    left, right = 1, max(times) * n
    
    while left < right:
        mid = (left + right) // 2
        total = 0
        
        # 시간에 나누어 사람 최대 수 구하기
        for time in times:
            total += mid // time
            
        if total >= n:
            right = mid
        else:
            left = mid + 1
            
    return right