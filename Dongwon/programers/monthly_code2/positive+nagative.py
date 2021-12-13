def solution(absolutes, signs):
    result = 0
    for sign, absolute in zip(absolutes, signs):
        if absolute:
            result += sign
        else:
            result -= sign
    return result