def solution(S):
    left = sum(map(int, list(S[:len(S)//2])))
    right = sum(map(int, list(S[len(S)//2:])))
    return "LUCKY" if left == right else "READY"


solution('123402')
solution('7755')