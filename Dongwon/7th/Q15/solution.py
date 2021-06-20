from collections import deque

def solution(N,M,K,X, graph_data):
    graph = [[] for __ in range(N+1)]
    for item in graph_data:
        graph[item[0]].append(item[1])
    distance = [-1] * (N+1)
    distance[X] = 0

    que = deque([X])
    while que:
        p = que.popleft()
        for item in graph[p]:
            if distance[item] == -1:
                distance[item] = distance[p] + 1
                que.append(item)
    
    # -1 체크를 위해 check 로직 추가
    check = False
    for i in range(len(distance)):
        if distance[i] == K:
            print(i)
            check = True
    if not check:
        print(-1)

solution(4,4,2,1, [[1,2],[1,3],[2,3],[2,4]])
solution(4,3,2,1, [[1,2],[1,3],[1,4]])
solution(4,4,1,1, [[1,2],[1,3],[2,3],[2,4]])