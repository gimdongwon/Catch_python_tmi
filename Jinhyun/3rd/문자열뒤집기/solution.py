def solution(inputs) :
    strlist = [i for i in input()]

    x = strlist[0]

    x_count = 0
    not_x_count = 0
    x_switch = 0

    for i in range(1, len(strlist)) :
        if x_switch == 0 and strlist[i] == x :
            x_count += 1
            x_switch = 1
        elif x_switch == 1 and strlist[i] == x :
            continue
        elif strlist[i] != x and x_switch == 1 :
            not_x_count += 1
            x_switch = 0
        elif strlist[i] != x and x_switch == 0 :
            continue

    return min(x_count, not_x_count)
