n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]

def quad_tree(x,y,n):
    check = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j] != check:
                print('(', end='')
                quad_tree(x,y,n//2)
                quad_tree(x,y+n//2, n//2)
                quad_tree(x+n//2,y, n//2)
                quad_tree(x+n//2,y+n//2, n//2)
                print(')', end='')
                return
    if check == 0:
        print('0', end='')
        return
    else:
        print('1', end='')
        return

quad_tree(0,0,n)