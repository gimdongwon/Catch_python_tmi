'''
오늘부터 N+1일째 되는 날 퇴사 위해 최대한 많은 상담
상담 완료 걸리는 기간 T_i, 받을 수 있는 금액 P_i
'''

# 1번 풀이 : 마지막 케이스에서 막힘 - 이유 : 상담할 수 있는 경우이지만 다음 상담이 더 큰 이득을 가져오는 경우
def solution_1(n, t, p) :
    time = list(map(int, t.split()))
    cost = list(map(int, p.split()))
    answer = []
    for i in range(n) :
        start = i
        pay = cost[start]
        if start + time[i] > n :
            break
        while True :
            print(start+1, cost[start], pay)
            start += time[start]
            if start >= n or start + time[start] > n:
                break
            pay += cost[start]
        answer.append(pay)
        print('-'*30)
    return max(answer)

# 2번 풀이 : 뒤에서부터 풀이 접근
def solution(n, t, p) :
    time = list(map(int, t.split()))
    cost = list(map(int, p.split()))
    dp = [0] * (n + 1)
    for i in range(n-1, -1, -1) :
        print(dp)
        if i + time[i] > n :
            dp[i] = dp[i+1]
        else :
            dp[i] = max(dp[i+1], cost[i] + dp[i+time[i]])
    return dp[0]

# print(solution(7, '3 5 1 1 2 4 2', '10 20 10 20 15 40 200'))
# print(solution(10,'1 1 1 1 1 1 1 1 1 1', '1 2 3 4 5 6 7 8 9 10'))
print(solution(10, '5 5 5 5 5 5 5 5 5 5', '10 9 8 7 6 10 9 8 7 6'))
# print(solution(10, '5 4 3 2 1 1 2 3 4 5', '50 40 30 20 10 10 20 30 40 50'))