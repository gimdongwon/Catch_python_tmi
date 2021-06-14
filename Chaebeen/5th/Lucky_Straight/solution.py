def solution(n):
    n_list = list(map(int, str(n)))
    # n_list = [int(a) for a in str(n)]
    mid = len(n_list) // 2
    if sum(n_list[:mid]) == sum(n_list[mid:]):
        print("LUCKY")
    else:
        print("READY")


solution(123402)
