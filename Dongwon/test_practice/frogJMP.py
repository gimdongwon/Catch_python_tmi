def solution(X, Y, D):
    # write your code in Python 3.6
    flag = (Y-X) // D
    remain = (Y-X) % D
    if remain == 0:
        return flag
    else:
        return flag + 1