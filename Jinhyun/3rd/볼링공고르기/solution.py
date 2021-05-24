from itertools import combinations as cb

def solution(first_line, second_line) :
    n, m = map(int, first_line.split())
    gram = list(map(int, second_line.split()))

    x = cb(gram, 2)
    list_gram = [i+j for i, j in x]
    n_count = len(list(filter(lambda x : x <= n, list_gram)))
    m_count = len(list(filter(lambda x : x <= m, list_gram)))
    return max(n_count, m_count)
