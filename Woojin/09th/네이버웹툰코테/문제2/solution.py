from collections import defaultdict

def get_graph(words):
    words = sorted(words, reverse=True)
    graph = defaultdict(list)
    
    for w1 in words:
        for w2 in words:
            graph[w1].append(w1 + w2)
            for w3 in words:
                graph[w1 + w2].append(w1 + w2 + w3)
                for w4 in words:
                    graph[w1 + w2 + w3].append(w1 + w2 + w3 + w4)
                    for w5 in words:
                        graph[w1 + w2 + w3 + w4].append(w1 + w2 + w3 + w4 + w5)
                        
    return graph

def solution(word):
    words = ["A", "E", "I", "O", "U"]
    graph = get_graph(words)
    
    for i, w in enumerate(words):
        if word[0] == w:
            order = 781 * i
    
    stack = [word[0]]
    
    while stack:
        w = stack.pop()
        order += 1
        
        if w == word:
            return order
        
        stack.extend(graph[w])