import re

def solution(S):
    print(S)
    strings = "".join(sorted(re.sub("[0-9]", "", S)))
    num = sum(map(int, list(re.sub("[A-Z]", "", S))))
    
    print(strings + str(num))

solution('K1KA5CB7')
solution('AJKDLSI412K4JSJ9D')