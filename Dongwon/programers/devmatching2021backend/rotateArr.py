def rotate(a,b,c,d, graph):
    # rotate하는 로직.
    # first = graph[a+1][b]
    pre = 0
    last = graph[c-1][d]
    nums = [last]
    for i in range(a,c+1):
        for j in range(b,d+1):
            if i == a or j == b or i== c or j == d:
                # 동쪽
                if i == a:
                    if j==b:
                        pre = graph[i][j]
                        graph[i][j] = graph[i+1][j]
                    else:
                        graph[i][j], pre = pre, graph[i][j]
                # 북쪽
                elif j == b:
                    if i != c:
                        graph[i][j] = graph[i+1][j]
                    else:
                        graph[i][j] = graph[i][j+1]
                # 남쪽
                elif j == d:
                    graph[i][j], pre = pre, graph[i][j]
                # 서쪽
                elif i == c:
                    graph[i][j], pre = graph[i][j+1], graph[i][j]
                nums.append(graph[i][j])
    graph[c][d] = last
    # print(graph)
    answer = min(nums)
    return graph, answer

def solution(rows, columns, queries):
    result = []
    # graph = [[i + (j * columns) for i in range(1,rows+1)] for j in range(rows)]
    graph = [[i + (j*columns) for i in range(1, columns+1)] for j in range(rows)]
    # print(graph)
    for x1,y1,x2,y2 in queries:
        graph, answer = rotate(x1-1,y1-1,x2-1,y2-1, graph)
        result.append(answer)
    return result