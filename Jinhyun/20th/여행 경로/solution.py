from collections import deque

def solution(tickets):
    tickets = sorted(tickets, key=lambda x : x[1])
    q = deque()
    for ind, i in enumerate(tickets) :
        if i[0] == 'ICN' :
            visited = [False for _ in range(len(tickets))]
            visited[ind] = True
            q.append([i,visited])
    while q :
        lists, visit = q.popleft()
        if sum(visit) == len(tickets) :
            return lists
        start, end = lists[-2], lists[-1]
        for i in range(len(tickets)) :
            tmp = lists[:]
            vis = visit[:]
            if not vis[i] and tickets[i][0] == end :
                vis[i] = True
                tmp.append(tickets[i][1])
                q.append([tmp, vis])