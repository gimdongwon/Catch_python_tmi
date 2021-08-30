import heapq

def solution(n, start, end, roads, traps):
    graph = [[] for _ in range(n)]
    start -= 1; end -= 1
    # 2차원 배열로 초기화 해야 하는데 traps수의 제곱으로 움직여야 해서 시프트 비트 연산자로 처리
    # n은 노드갯수로 2차원배열은 traps의 갯수로
    isVisit = [[False] * n for _ in range(1<<len(traps))]
    trap_dict = {trap-1: idx for idx, trap in enumerate(traps)}
    
    # 방향으로 구분하여 시작, 끝 노드 정함.
    for s,e,t in roads:
        graph[s-1].append([e-1,t,0])
        graph[e-1].append([s-1,t,1])
    
    que = []
    heapq.heappush(que, (0, start,0))
    
    while que:
        cur_time, cur_node, state = heapq.heappop(que)
        # 도착했으면 return
        if cur_node == end:
            return cur_time
        # 이미 방문함.
        if isVisit[state][cur_node] == True:
            continue
         # 미 방문시 방문 처리
        else:
            isVisit[state][cur_node] = True
        
        # 다음 노드를 계산함
        # 현재 노드와 다음 노드의 trap 밟는 경우에 따라서 분기처리
        for next_node, next_cost, road_type in graph[cur_node]:
            next_state = state
            cur_trap = 1 if cur_node in trap_dict else 0
            next_trap = 1 if next_node in trap_dict else 0
            
            # 현재, 다음 trap 없음
            if cur_trap == 0 and next_trap == 0:
                if road_type == 1:
                    continue
            # 현재나 다음 둘 중하나가 trap에 속함.
            elif (cur_trap + next_trap) == 1:
                node_idx = cur_node if cur_trap == 1 else next_node
                isTrapOn = (state & (1<<trap_dict[node_idx]))>>trap_dict[node_idx]
                if isTrapOn != road_type:
                    continue
            # 둘다 trap임.
            else:
                isTrapOn = (state & (1<<trap_dict[cur_node]))>>trap_dict[cur_node]
                n_isTrapOn = (state & (1<<trap_dict[next_node]))>>trap_dict[next_node]
                if (isTrapOn ^ n_isTrapOn) != road_type:
                    continue
            if next_trap == 1:
                next_state = state ^ (1<<trap_dict[next_node])
            heapq.heappush(que, (next_cost + cur_time ,next_node, next_state))
                
            