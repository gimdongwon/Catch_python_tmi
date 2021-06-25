from itertools import permutations

def solution(n, weak, dist):
    # 친구들이 주기적으로 취약지점 점검
    # 점검시간 1시간
    # 최소한의 친구들을 투입
    leng = len(weak)
    for i in range(leng):
        weak.append(weak[i] + n)
    answer = len(dist) + 1
    
    # 시작지점 선택
    for start in range(leng):
        # 친구가 1시간 안에 이동할 수 있는 거리의 조합
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count-1]
            print(start, friends, count, position, weak)
            for idx in range(start, start+leng):
                if position < weak[idx]:
                    count+=1
                    if count > len(dist):
                        break
                    position = weak[idx]+friends[count-1]
            answer = min(answer, count)
    # 전부 점검할 수 없는 경우
    if answer > len(dist):
        return -1
    return answer


print(solution(12,[1,5,6,10],[1,2,3,4])) # 2
print(solution(12,[1,3,4,9,10],[3,5,7])) # 1