def solution(first_line) :
    number = 0
    str_list = []
    for i in first_line :
        try :
            if isinstance(int(i), int) :
                number += int(i)
        except :
            str_list.append(i)
    str_list.sort()
    number = str(number)
    str_list.append(number)
    return ''.join(str_list)

print(solution('K1KA5CB7'))
print(solution('AJKDLSI412K4JSJ9D'))