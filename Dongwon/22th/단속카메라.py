# 1차시도

def solution(routes):
    routes.sort()
    result = 0
    start = routes[0][0]
    end = routes[-1][1]
    time = start
    pre_cnt = 1
    while time <= end:
        cnt = 0
        for route in routes:
            s,e = route
            if s <= time <= e:
                cnt += 1
        # print(cnt, time)
        if pre_cnt < cnt:
            result += 1
        pre_cnt = cnt
        time+=1
    return result