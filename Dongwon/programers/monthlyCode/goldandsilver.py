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