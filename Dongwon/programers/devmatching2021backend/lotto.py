from collections import defaultdict

def solution(lottos, win_nums):
    ranking_dict = defaultdict(int)
    ranking_dict[0] = 6
    
    for i in range(1,7):
        ranking_dict[i] = 7-i
    
    cnt = 0
    
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
            win_nums.remove(lotto)
    
    best = 0
    
    if lottos.count(0) <= len(win_nums):
        best = cnt + lottos.count(0)
    else:
        best = cnt + len(win_nums)
    
    return [ranking_dict[best], ranking_dict[cnt]]