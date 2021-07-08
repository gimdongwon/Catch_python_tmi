# 시간 초과 3개

def solution(N, stages):
    result = {}
    for i in range(N):
        cur_users = stages.count(i+1)
        clear_users = len(list(filter(lambda x: x>=i+1, stages)))
        if clear_users:
            result[i+1] = cur_users / clear_users
        else:
            result[i+1] = 0
    
    result = sorted(result.items(), key= lambda x: x[1], reverse=True)
    return [item[0] for item in result]


# 성공

def solution(N, stages):
    result = {}
    clear_users = 0
    for i in range(N):
        cur_users = stages.count(i+1)
        if cur_users != 0:
            # filter 제거
            result[i+1] = cur_users / (len(stages) - clear_users)
        else:
            result[i+1] = 0
        clear_users += cur_users
        
    result = sorted(result.items(), key= lambda x: x[1], reverse=True)
    return [item[0] for item in result]
