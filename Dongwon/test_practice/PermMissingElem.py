# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    graph = [0 for _ in range(len(A)+1)]
    
    for i in range(len(A)):
        graph[i-1] = 1

    return graph.index(0) + 1