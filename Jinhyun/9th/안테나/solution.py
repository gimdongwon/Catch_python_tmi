def solution(n : int, homes : str) :
    homes = sorted(list(map(int, homes.split())))
    return (homes[(n-1) // 2])
    '''
    < 중앙값 생각 안하고 짠 코드>
    min_val = int(1e9)
    index = 0
    for i in range(homes[-1]) :
        total_distance = 0
        for j in homes :
            total_distance += abs(i - j)
        if total_distance < min_val :
            min_val = total_distance
            index = i
    return index
    '''
print(solution(4, '5 1 7 9'))