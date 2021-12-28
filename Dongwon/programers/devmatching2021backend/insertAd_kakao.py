def parseIntTime(time):
    h,m,s = time.split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)

def toStringTime(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s

def solution(play_time, adv_time, logs):
    answer = ''
    play_time = parseIntTime(play_time)
    adv_time = parseIntTime(adv_time)
    all_time = [0 for i in range(play_time+1)]
    
    # 시작, 끝 지점  표기
    for log in logs:
        start, end = log.split("-")
        start = parseIntTime(start)
        end = parseIntTime(end)
        all_time[start] += 1
        all_time[end] -= 1
    
    # 중간 지점 표기
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i-1]
        
    # 누적 지점 표기
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i-1]
        
    max_viewers = 0
    max_time = 0
    
    # 계산
    for i in range(adv_time-1, play_time):
        if i >= adv_time:
            if max_viewers < all_time[i] - all_time[i-adv_time]:
                max_viewers = all_time[i] - all_time[i-adv_time]
                max_time = i - adv_time + 1
        else:
            if max_viewers < all_time[i]:
                max_viewers = all_time[i]
                max_time = i - adv_time + 1
    return toStringTime(max_time)
    
    print(toStringTime(max_time))