def solution(N, num_list, operater):
    min_num = float("inf")
    max_num = float("-inf")

    def dfs(now, level):
        if level == N:
            nonlocal min_num, max_num
            min_num = min(min_num, now)
            max_num = max(max_num, now)
        if operater[0] > 0:
            operater[0] -= 1
            dfs(now + num_list[level], level + 1)
            operater[0] += 1
        if operater[1] > 0:
            operater[1] -= 1
            dfs(now - num_list[level], level + 1)
            operater[1] += 1
        if operater[2] > 0:
            operater[2] -= 1
            dfs(now * num_list[level], level + 1)
            operater[2] += 1
        if operater[3] > 0:
            result = abs(now)//num_list[level]
            if now < 0:
                result *= -1
            operater[3] -= 1
            dfs(result, level+1)
            operater[3] += 1
    now = num_list[0]
    dfs(now, 1)
    print(max_num)
    print(min_num)


solution(2,[5,6],[0,0,1,0])
solution(3,[3,4,5],[1,0,1,0])
solution(6,[1,2,3,4,5,6],[2,1,1,1])