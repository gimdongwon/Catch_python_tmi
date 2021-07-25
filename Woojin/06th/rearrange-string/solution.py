# 풀이 1
from re import findall

def solution(s):
    upper_alphabet = findall("[A-Z]", s)
    number = sum(map(int, findall("[0-9]", s)))
    
    if number != 0:
        return "".join(sorted(upper_alphabet)) + str(number)
    else:
        return "".join(sorted(upper_alphabet))

print(solution("AJKDLSI412K4JSJ9D")) # "ADDIJJJKKLSS20"
print(solution("A9H3N1W2O2O3JIN")) # "AHIJNNOOW20"
print(solution("AJKDLSIKJSJD")) # "ADDIJJJKKLSS"

# 풀이 2

def solution(s):
    result = []
    number = 0

    for char in s:
        if ord(char) <= 57: # 숫자는 48 ~ 57, 알파벳 대문자는 65 ~ 90
            number += int(char)
        else:
            result.append(char)

    result.sort()

    if number != 0:
        result.append(str(number))

    return "".join(result)

# 풀이 3

def solution(s):
    result = []
    number = 0

    for char in s:
        try:
            if isinstance(int(char), int):
                number += int(char)
        except ValueError:
            result.append(char)

    result.sort()

    if number != 0:
        result.append(str(number))

    return "".join(result)