def plus_move(start, end, data) :
    if start > end :
        plus_data = sum(data[end : start])
        if plus_data == 0 :
            return end
        else :
            return plus_move(end, end - plus_data, data)
    else :
        plus_data = sum(data[start+1 : end+1])
        if plus_data == 0 :
            return end
        else :
            return plus_move(end, end + plus_data, data)

def move(k, num, select, data) :
    if select == "U" :
        return plus_move(k, k - num, data)
    else:
        return plus_move(k, k + num, data)
    
    
def solution(n, k, cmd):
    data = [False] * n
    command_index = []
    for element in cmd :
        if len(element) > 1 :
            select, num = element.split()
            k = move(k, int(num), select, data)
        else :
            if element == "C" :
                data[k] = True
                command_index.append(k)
                while data[k] and sum(data[k:]) == len(data) - k :
                    k -= 1
            else :
                undo = command_index.pop()
                data[undo] = False
                
    return ''.join(['O' if not i else 'X' for i in data])

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
