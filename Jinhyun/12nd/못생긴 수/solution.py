'''
못생긴 수 : 2, 3, 5만을 소인수로 가지는 수
1은 못생긴 수라고 가정
'''
from collections import defaultdict
import time
# 소인수 분해 함수
def get_factorization(num) :
    dic = defaultdict(int)
    d = 2
    while d <= num :
        if num % d == 0 :
            dic[d] += 1
            num = num // d
        else :
            d += 1
    return dic

def solution(n) :
    n = n - 1
    count = 1
    prime_factor = [2, 3, 5]
    while n :
        on_off = True
        count += 1
        for i in get_factorization(count).keys() :
            if i not in prime_factor :
                on_off = False
                break
        if on_off :
            n -= 1
    return count

print(get_factorization(8))