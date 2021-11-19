n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]
result = [0,0,0]

def check_square(x,y,m):
    global result
    pick = graph[x][y]
    for i in range(x, x+m):
        for j in range(y, y+m):
            if graph[i][j] != pick:
                new_m = m // 3
                for k in range(3):
                    for t in range(3):
                        check_square(x + k*new_m, y + t*new_m, new_m)
                return
    
    result[graph[x][y]+1] += 1

check_square(0,0,n)

print(result)