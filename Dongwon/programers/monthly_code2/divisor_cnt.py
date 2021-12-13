def find_divisor(n):
    result = 0
    for i in range(1, n+1):
        if n % i == 0:
            result += 1
    return result

def solution(left, right):
    arr = [item for item in range(left, right+1)]
    result = 0
    
    for item in arr:
        cnt = find_divisor(item)
        if cnt % 2 == 0:
            result += item
        else:
            result -= item
    
    return result