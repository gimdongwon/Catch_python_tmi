from collections import deque

def solution(m,n,h, tomatos):
    dx = [-1,1,0,0,0,0]
    dy = [0,0,-1,1,0,0]
    df = [0,0,0,0,-1,1]
    day = 0
    ripen_tomatos = []
    for floor in range(h):
        for i in range(n):
            for j in range(m):
                if tomatos[floor][i][j] == 1:
                    ripen_tomatos.append([day,[floor,i,j]])
    
    queue = deque(ripen_tomatos)
    while queue:
        day, which = queue.popleft()
        f,x,y = which
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nf = f + df[i]
            if -1 < nf < h and -1 < nx < n and -1 < ny < m and tomatos[nf][nx][ny] == 0:
                queue.append([day+1, [nf,nx,ny]])
                tomatos[nf][nx][ny] = 1

    
    for tomato in tomatos:
        for item in tomato:
            for j in item:
                if j == 0:
                    print(-1)
                    exit(0)
            day = max(day, max(item))
            # if 0 in item:
            #     print(-1)
            #     break
    print(day)

# solution(5,3,1, [[[0,-1,0,0,0],[-1,-1,0,1,1],[0,0,0,1,1]]])
solution(5,3,2, [[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0]]])
solution(4,3,2, [[[1,1,1,1],[1,1,1,1],[1,1,1,1]],[[1,1,1,1],[-1,-1,-1,-1],[1,1,1,-1]]])