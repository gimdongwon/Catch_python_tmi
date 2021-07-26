def solution(n, triangle) :
    up, down = 0, 0
    for i in range(1, n) :
        for j in range(len(triangle[i])) :
            if j == 0 :
                up = 0
            else :
                up = triangle[i-1][j-1]
            if j == len(triangle[i]) - 1 :
                down = 0
            else :
                down = triangle[i-1][j]
            triangle[i][j] += max(up, down)

    return max(triangle[-1])

print(solution(5,[[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]))