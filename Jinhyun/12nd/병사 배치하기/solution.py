'''
N명의 병사 무작위 나열
각 병사 특정값 전투력 보유
병사 배치할 경우 : 전투력 높은 순 내림차순
배치과정 열외 - 남아있는 병사 수 최대가 되도록
'''

def solution(n, soldiers) :
    soldiers.reverse()

    dp = [1] * n
    for i in range(1, n) :
        for j in range(0, i) :
            # 해당 지점 전 모든 숫자 포함시키기 위해서
            if soldiers[i] > soldiers[j] :
                dp[i] = max(dp[i], dp[j] + 1)
            
        print(dp)
    return n - max(dp)

print(solution(8, [15, 16, 4, 8, 5, 3, 2, 4]))

