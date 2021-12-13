import math

def solution(a, b, g, s, w, t):
    arr = []
    for i in range(len(g)):
        gold, silver, time, remain = 0,0,0,0
        gold_flag = 0
        while True:
            # print(i, gold, silver, time)
            if gold < a and g[i] > 0:
                gold += w[i]
                time += t[i] * 2
                g[i] -= w[i]
                if gold <= a:
                    continue
                else:
                    time -= t[i] * 2
                    ramain = gold - a
            if silver < b and s[i] > 0:
                silver += w[i] if not remain else w[i] - remain
                s[i] -= w[i]
                remain = 0
                time += t[i] * 2
                if silver <= b:
                    continue
            break
        # print(i, gold, silver, time, "break")
        arr.append(time - t[i])
        
    return max(arr)

# 맞은 풀이
def solution2(a, b, g, s, w, t):
    result = []
    start, end = 0, (10 ** 9) * (10 ** 5) * 4
    while start <= end:
        mid = (start + end) // 2
        gold, silver, total = 0,0,0
        
        for i, time in enumerate(t):
            cnt = (mid - time) // (time * 2) + 1

            if cnt * w[i] > g[i]:
                gold += g[i]
            if cnt * w[i] <= g[i]:
                gold += cnt * w[i]
            if cnt * w[i] > s[i]:
                silver += s[i]
            if cnt * w[i] <= s[i]:
                silver += cnt * w[i]
            if s[i] + g[i] < cnt * w[i]:
                total += s[i] + g[i]
            if s[i] + g[i] >= cnt * w[i]:
                total += cnt * w[i]

        if gold >= a and silver >= b and total >= a + b:
            end = mid - 1
            result.append(mid)
            # result = min(result, mid)
        else:
            start = mid + 1
    
    return min(result)
        