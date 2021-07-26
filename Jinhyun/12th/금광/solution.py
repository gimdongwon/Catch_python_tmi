'''
금광의 크기 : N * M
각 칸은 특정한 크기의 금이 들어있음
첫번째 열의 어느 행에서든 출발 가능 - 이후 m번에 걸쳐 이동해야함
'''

def solution(t, n, m, case) :
    # 금광 2차원 배열 생성
    case = list(map(int, case.split()))
    cases = []
    for i in range(n) :
        cases.append(case[i*m : i*m+m])

    # 3가지 경우 계산
    top, mid, bot = 0, 0, 0
    for i in range(1, m) :
        for j in range(n) :
            if j == 0 :
                top = 0
            else :
                top = cases[j-1][i-1]
            if j == n-1 :
                bot = 0
            else :
                bot = cases[j+1][i-1]
            mid = cases[j][i-1]
            cases[j][i] += max(top, mid, bot)
    
    answer = 0
    for i in zip(*cases) :
        answer = max(answer, max(i))
    return answer

print(solution(2, 3, 4, '1 3 3 2 2 1 4 1 0 6 4 7'))
print(solution(2, 4, 4, '1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2'))