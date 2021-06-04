def solution(line) :
    lists = [int(i) for i in line]
    answer = 0
    for i in lists :
        if answer == 0 or answer == 1 or i == 0 or i == 1:
            answer += i
        else :
            answer *= i
    return answer


print(solution('02984'))
print(solution('567'))
print(solution('01901'))