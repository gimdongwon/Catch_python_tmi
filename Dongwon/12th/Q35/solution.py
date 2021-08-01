# 1차 풀이

def solution(n):
    ugly_nums = [0] * n # 0이 포함이 안됨.
    ugly_nums[0] = 1

    i2 = i3 = i5 = 0

    next2, next3, next5 = 2,3,5
    for i in range(1,n):
        # print(next2, next3, next5, " next")
        # print(i2,i3,i5, " i")
        ugly_nums[i] = min(next2,next3,next5)
        if ugly_nums[i] == next2:
            i2 += 1
            next2 = ugly_nums[i2] * 2
        if ugly_nums[i] == next3:
            i3 += 1
            next3 = ugly_nums[i3] * 3
        if ugly_nums[i] == next5:
            i5 += 1
            next5 = ugly_nums[i5] * 5
    print(ugly_nums)
    print(ugly_nums[n-1])

solution(14)