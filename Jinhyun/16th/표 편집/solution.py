from collections import defaultdict

def solution(n, k, cmd):
    dicts = defaultdict(list)
    dicts[0] = [n-1, 1]
    for i in range(1, n-1) :
        dicts[i] = [i - 1, i + 1]
    dicts[n-1] = [n-2, 0]
    reset = []
    for c in cmd :
        cnt = 0
        if len(c) != 1 :
            move, count = c.split()
            if move == "D" :
                while cnt < int(count) :
                    k = dicts[k][1]
                    cnt += 1
            elif move == "U" :
                while cnt < int(count) :
                    k = dicts[k][0]
                    cnt += 1
        else :
            move = c
            if move == "C" :
                dicts[dicts[k][0]][1] = dicts[k][1]
                dicts[dicts[k][1]][0] = dicts[k][0]
                reset.append((k, dicts[k]))
                tmp = dicts[k]
                del dicts[k]

                if tmp[1] == 0 :
                    k = tmp[0]
                else :
                    k = tmp[1]
                
            elif move == "Z" :
                num, node = reset.pop()
                dicts[node[0]][1] = num
                dicts[node[1]][0] = num
                dicts[num] = node
    print(dicts)
    answer = ''
    for i in range(n) :
        if dicts[i] :
            answer+='O'
        else :
            answer+='X'
    return answer

# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
