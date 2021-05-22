# coding=utf-8

def form_group(n, fear_level):
    result = 0  # 총 그룹 수
    group = 0  # 그룹 인원
    fear_level.sort()
    for i in range(len(fear_level)):
        group += 1
        if group >= fear_level[i]:
            result += 1
            group = 0

    return result


# n = input("number of member: ")
# x = [x for x in input("fear_level: ")]
# x = list(map(int, input("fear_level: ").split()))
# print(form_group(n, x))
print(form_group(5, [1, 1, 1, 2, 2]))
