n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0 # 1

def check(x,y,n):
    global white, blue
    color = graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != graph[i][j]:
                check(x,y,n//2)
                check(x,y+n//2,n//2)
                check(x+n//2,y,n//2)
                check(x+n//2,y+n//2,n//2)
                return
    if color == 0:
        white += 1 
    else:
        blue += 1

check(0,0,n)
print(white)
print(blue)