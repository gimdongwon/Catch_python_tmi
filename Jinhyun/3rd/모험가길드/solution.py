def solution(first_line, second_line)

    num = int(first_line)
    people = list(map(int, second_line.split()))

    people.sort()

    group = 0
    count = 0
    # 남은 친구들은 처음 group에 넣어줌
    for i in people :
        count += 1
        if count >= i :
            group += 1
            count = 0
    return group
