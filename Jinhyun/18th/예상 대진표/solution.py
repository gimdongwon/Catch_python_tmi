def solution(n,a,b):
    answer = 0
    participant = [i for i in range(1,n+1)]
    onoff = 1
    while onoff :
        lists = []
        answer += 1
        for i in range(0, n, 2) :
            if a in participant[i:i + 2] and b in participant[i:i + 2] :
                onoff = 0
                break
            if a in participant[i:i + 2] :
                lists.append(a)
            elif b in participant[i:i + 2] :
                lists.append(b)
            else :
                lists.append(participant[i])
        participant = lists
        n = n // 2
    return answer