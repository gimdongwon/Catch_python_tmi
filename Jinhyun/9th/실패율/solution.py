def solution(N, stages):
    ns = {}
    for i in range(1, N+1) :
        count = 0
        fail = 0
        for j in stages :
            if i <= j :
                count += 1
            if i == j :
                fail += 1
        try :
            ns[i] = fail/count
        except :
            ns[i] = 0
    ns = sorted(ns.items(), key = lambda item : item[1], reverse=True)
    answer = [i[0] for i in ns]
    return answer

print(solution(5, [2,1,2,6,2,4,3,3]))
print(solution(4, [4,4,4,4,4]))