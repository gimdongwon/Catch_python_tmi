# --- 프로그래머스 스타일(첫 풀이) ---

from copy import deepcopy
from itertools import permutations

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def get_answer(sequence, operator):    
    for oper in operator:
        if oper == "/":
            x = sequence[0]
            y = sequence[1]
            sequence[:2] = [(sign(x)*sign(y)) * (abs(x)//abs(y))]
        else:
            x = str(sequence[0])
            y = str(sequence[1])
            sequence[:2] = [eval(x + oper + y)]
    
    return sequence[0]
    
def solution(sequence, operator_info):
    base_operator = operator_info[0] * "+" + operator_info[1] * "-" + operator_info[2] * "*" + operator_info[3] * "/"
    result = []
    
    for operator in set(permutations(base_operator, len(base_operator))):
        sequence_copy = deepcopy(sequence)
        result.append(get_answer(sequence_copy, operator))
    
    return [max(result), min(result)]
    
print(solution([5, 6], [0, 0, 1, 0])) # [30, 30]
print(solution([3, 4, 5], [1, 0, 1, 0])) # [35, 17]
print(solution([1, 2, 3, 4, 5, 6], [2, 1, 1, 1])) # [54, -24]

# --- 백준 스타일(개선된 풀이) ---

from itertools import permutations

def get_answer(sequence, operator):
    answer = sequence[0]
    
    for num, oper in zip(sequence[1:], operator):
        if oper == "/":
            answer = int(answer / num)
        else:
            answer = eval(str(answer) + oper + str(num))
    
    return answer
    
N = int(input())
sequence = list(map(int, input().split(" ")))
plus, minus, time, divide = map(int, input().split(" "))
base_operator = plus * "+" + minus * "-" + time * "*" + divide * "/"
max_answer = -float("inf")
min_answer = float("inf")

for operator in set(permutations(base_operator, len(base_operator))):
    answer = get_answer(sequence, operator)
    max_answer = max(max_answer, answer)
    min_answer = min(min_answer, answer)

print(max_answer)
print(min_answer)

# --- 모범 답안 ---

n = int(input())
num = list(map(int, input().split()))
plus, minus, time, divide = map(int, input().split())

min_ans = int(1e9)
max_ans = -int(1e9)

# 백트래킹 -> 해를 찾는 도중에 막히면 되돌아가서 다시 해를 찾는 기법 -> 재귀를 이용한 완전 검색
def solution(cnt, tot):
    global plus, minus, time, divide, min_ans, max_ans

    # n번째 인덱스까지 도달시 max, min 수정하고 다른 경우로 돌아가기
    if cnt == n:
        max_ans = max(max_ans, tot)
        min_ans = min(min_ans, tot)
        return
    
    # 재귀적 사고
    if plus > 0:
        plus -= 1
        solution(cnt + 1, tot + num[cnt])
        plus += 1

    if minus > 0:
        minus -= 1
        solution(cnt + 1, tot - num[cnt])
        minus += 1

    if time > 0:
        time -= 1
        solution(cnt + 1, tot * num[cnt])
        time += 1

    if divide > 0:
        divide -= 1
        solution(cnt + 1, int(tot / num[cnt]))
        divide += 1


solution(1, num[0])
print(max_ans)
print(min_ans)