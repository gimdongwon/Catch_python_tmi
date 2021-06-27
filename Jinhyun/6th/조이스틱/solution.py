# 65 : A / 90 : Z
def alphabet_to_a(alphabet) :
    if ord(alphabet) > 77 :
        return ord('Z') - ord(alphabet) + 1
    else :
        return ord(alphabet) - ord('A')

def solution(name):
    name_list = [1 if i != 'A' else 0 for i in name]
    name_sum = sum(name_list)
    change_val = sum([alphabet_to_a(i) for i in name])
    start = 0
    answer = 0
    length_one = 1
    while sum(name_list) != 0 :
        if name_list[start] == 1 :
            name_list[start] = 0
        elif name_list[start + length_one] == 1:
            answer += length_one
            name_list[start + length_one] = 0
            start += length_one
            length_one = 1
        elif name_list[start - length_one] == 1 :
            answer += length_one
            name_list[start - length_one] == 0
            start -= length_one
            length_one = 0
        else :
            length_one += 1
        print('name_list : '+str(name_list))
        print('answer : '+str(answer))
        print('start : ' + str(start))
        print('length_one : '+str(length_one))
    print('value : ' + str(change_val))
    return answer + change_val

print(solution("JAN"))
print(solution("ABAAAAAAAAABB"))
