# n = int(input())
n = 7
graph = {
    'A': ['B','C'],
    'B': ['D','.'],
    'C': ['E','F'],
    'D': ['.','.'],
    'E': ['.','.'],
    'F': ['.','G'],
    'G': ['.','.']
}
board = {
    'A': ['.'],
    'B': ['A'],
    'C': ['A'],
    'D': ['B'],
    'E': ['C'],
    'F': ['C'],
    'G': ['F']
}
# graph = dict()

visited = {
    'A': False,
    'B': False,
    'C': False,
    'D': False,
    'E': False,
    'F': False,
    'G': False,
}

# for _ in range(n):
#     parent, left, right = input().split()
#     graph[parent] = [left, right]

def find_left(x):
    if graph[x][0] == '.':
        return x
    else:
        return find_left(graph[x][0])

# start = find_left('A')

def front_search(x):
    print(x, end='')
    if graph[x][0] != '.':
        front_search(graph[x][0])
    if graph[x][1] != '.':
        front_search(graph[x][1])
    
def middle_search(x):
    print(x, end='')
    visited[x] = True
    if list(visited.values()).count(True) == n:
        return
    if board[x][0] != '.':
        if visited[board[x][0]] == False:
            middle_search(board[x][0])
        else:
            target = find_left(graph[x][1])
            # print(target, "$")
            middle_search(graph[x][1])
    else:
        target = find_left(graph[x][1])
        # print(target, "@")
        middle_search(target)

def back_search(x):
    if x != '.':
        back_search(graph[x][0])
        back_search(graph[x][1])
        print(x, end='')

front_search('A') # 전위 순회
print()
middle_search('D')
print()
back_search('A')
print()