import sys
input = sys.stdin.readline

n = int(input())
graph = {}

for _ in range(n):
    parent, left, right = input().strip().split()
    graph[parent] = [left, right]

def front_search(x):
    if x != '.':
        print(x, end='')
        front_search(graph[x][0])
        front_search(graph[x][1])
    
def post_search(x):
    if x != '.':
        post_search(graph[x][0])
        print(x, end='')
        post_search(graph[x][1])
        
def back_search(x):
    if x != '.':
        back_search(graph[x][0])
        back_search(graph[x][1])
        print(x, end='')

front_search('A') # 전위 순회
print()
post_search('A')
print()
back_search('A')