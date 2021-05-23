def choose_ball(ball_list):
    result = 0
    for i in range(len(ball_list)):
        for j in range(i + 1, len(ball_list)):
            if ball_list[i] != ball_list[j]:
                result += 1

    return result


print (choose_ball([1, 3, 2, 3, 2]))
