from itertools import permutations

def solution(expression):
    candiates = ["*", "+", "-"]
    answer = []
    for candiate in permutations(candiates, 3):
        temp_list = []
        a, b = candiate[0],candiate[1]
        for e in expression.split(a):
            temp = [f'({i})' for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)