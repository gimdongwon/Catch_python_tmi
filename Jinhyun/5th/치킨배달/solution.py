from itertools import combinations as cb

def distance(x, y) :
    # x = (r1, c1), y = (r2, c2)
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def location(n, matrix) :
    home = []
    chicken = []
    for index, i in enumerate(matrix) :
        if i == '1' :
            home.append((index // n, index % n))
        if i == '2' :
            chicken.append((index // n, index % n))

    return home, chicken

def solution(n, m, matrix) :
    home, chicken = location(n, matrix)
    answer = []
    for chic in cb(chicken, m) :
        min_val = 0
        for ho in home :
            min_val += min([distance(i, ho) for i in chic])
        answer.append(min_val)

    return min(answer)
    

print(solution(5, 3, '0010000201012000010000002'))
print(solution(5, 2, '0201010100000002001122012'))
print(solution(5, 1, '1200012000120001200012000'))
