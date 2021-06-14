from re import findall

def solution(S):
    upper_alphabet = findall("[A-Z]", S)
    number = sum(map(int, findall("[0-9]", S)))  
    
    return "".join(sorted(upper_alphabet)) + str(number)

print(solution("AJKDLSI412K4JSJ9D")) # "ADDIJJJKKLSS20"
print(solution("A9H3N1W2O2O3JIN")) # "AHIJNNOOW20"