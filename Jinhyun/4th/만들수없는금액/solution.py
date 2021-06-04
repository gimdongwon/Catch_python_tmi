from itertools import combinations as cb

def solution(first_line, second_line) :
    first_line = int(first_line)
    second_line = list(map(int, second_line.split()))
    answer = [0] * (sum(second_line) + 1)
    for i in range(1, first_line + 1) :
        val = list(cb(second_line, i))
        val = [sum(j) - 1 for j in val]
        for j in val :
            answer[j] = 1
    return answer.index(0) + 1

print(solution('5', '3 2 1 1 9'))
print(solution('3', '3 5 7'))
print(solution('5', '1 2 3 4 5'))