from collections import deque

def comparison(word, list_word) :
    tmp = 0
    for i in range(len(word)) :
        if word[i] != list_word[i] :
            tmp += 1
        if tmp == 2 :
            return False
    return True

def solution(begin, target, words):
    if target not in words :
        return 0
    visited = [False for _ in range(len(words))]
    q = deque()
    q.append([begin, 0])
    while q :
        word, cost = q.popleft()
        if word == target :
            return cost
        for i in range(len(words)) :
            if not visited[i] and comparison(word, words[i]) :
                visited[i] = True
                q.append([words[i], cost + 1])
    return 0