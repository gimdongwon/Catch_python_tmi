import sys
input = sys.stdin.readline

# n = int(input())
# tree_parents = list(map(int, input().split()))
# delete_node = int(input())

# graph = [[] for _ in range(n)]

# for i in range(n):
#     if tree_parents[i] != -1:
#         graph[tree_parents[i]].append(i)

# # delete node

# stack = []

# stack.append(delete_node)
# while stack:
#     target = stack.pop()
#     for i in range(len(graph[target])):
#         stack.append(graph[target][i])
#     for i in range(len(graph)):
#         if delete_node in graph[i]:
#             graph[i].remove(delete_node)
    

# result = []

# for i in range(len(graph)):
#     for j in range(len(graph[i])):
#         if graph[i]:
#             if not graph[graph[i][j]]:
#                 result.append(graph[i][j])

# print(len(result))

n = int(input())
tree_parents = list(map(int, input().split()))
delete_node = int(input())

def dfs(num, tree_parents):
    tree_parents[num] = -2
    for i in range(len(tree_parents)):
        if num == tree_parents[i]:
            dfs(i, tree_parents)

result = 0
dfs(delete_node, tree_parents)

for i in range(len(tree_parents)):
    if tree_parents[i] != -2 and i not in tree_parents:
        result += 1
print(result)