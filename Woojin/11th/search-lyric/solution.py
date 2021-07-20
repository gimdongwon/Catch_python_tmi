# --- 프로그래머스 스타일 ---
# 다섯 번 시도 만에 성공

# --- 첫 번째 시도 ---
# 효율성 3개 실패

from collections import defaultdict
from re import search

def get_word_dict(words):
    word_dict = defaultdict(list)
    
    for word in words:
        word_dict[len(word)].append(word)
    
    return word_dict


def solution(words, queries):
    word_dict = get_word_dict(words)
    result = []
    
    for query in queries:
        query = query.replace("?", ".")
        result.append(sum(1 for word in word_dict[len(query)] if search(query, word)))
        
    return result

# --- 두 번째 시도 ---
# 효율성 2개 실패

from collections import defaultdict

def get_word_dict(words):
    word_dict = defaultdict(list)
    
    for word in words:
        word_dict[len(word)].append(word)
    
    for value in word_dict.values():
        value.sort()
    
    return word_dict

def get_wildcard_idx(query):
    if query[0] == "?" and query[-1] == "?":
        return (0, len(query) - 1)
    
    start = 0
    end = len(query)
    
    if query[0] == "?":    
        while start <= end:
            mid = (start+end) // 2
            
            if mid == start:
                break
            
            if query[mid] == "?":
                start = mid
            else:
                end = mid
        
        return (0, mid)
    else:
        while start <= end:
            mid = (start+end) // 2
            
            if mid == start:
                break
            
            if query[mid] == "?":
                end = mid
            else:
                start = mid
        
        return (mid + 1, len(query) - 1)


def search_lyric(words, query):
        idx = get_wildcard_idx(query)
        
        if idx == (0, len(query) - 1):
            return len(words)
        
        if idx[0] == 0:
            query = query[idx[1] + 1:]

            return sum(1 for word in words if word[idx[1] + 1:] == query)
        else:
            query = query[:idx[0]]
            
            return sum(1 for word in words if word[:idx[0]] == query)

def solution(words, queries):
    word_dict = get_word_dict(words)
    
    return [search_lyric(word_dict[len(query)], query) for query in queries]

# --- 세 번째 시도 ---
# 효율성 3개 실패

from collections import defaultdict
from itertools import chain

def get_word_dict(words):
    len_dict = defaultdict(list)
    
    for word in words:
            len_dict[len(word)].append(word)
    
    len_dict = dict(len_dict)
    
    for key, value in len_dict.items():
        first_dict = defaultdict(list)
        last_dict = defaultdict(list)

        for v in value:
            first_dict[v[0]].append(v)
            last_dict[v[-1]].append(v)

        len_dict[key] = [first_dict, last_dict]

    return len_dict

def get_wildcard_idx(query):
    if query[0] == "?" and query[-1] == "?":
        return (0, len(query) - 1)
    
    start = 0
    end = len(query)
    
    if query[0] == "?":    
        while start <= end:
            mid = (start+end) // 2
            
            if mid == start:
                break
            
            if query[mid] == "?":
                start = mid
            else:
                end = mid
        
        return (0, mid)
    else:
        while start <= end:
            mid = (start+end) // 2
            
            if mid == start:
                break
            
            if query[mid] == "?":
                end = mid
            else:
                start = mid
        
        return (mid + 1, len(query) - 1)


def search_lyric(words, query):
        idx = get_wildcard_idx(query)
        
        if idx == (0, len(query) - 1):
            return len(words)
        
        if idx[0] == 0:
            query = query[idx[1] + 1:]
                
            return sum(1 for word in words if word[idx[1] + 1:] == query)
        else:
            query = query[:idx[0]]
            
            return sum(1 for word in words if word[:idx[0]] == query)

def solution(words, queries):
    word_dict = get_word_dict(words)
    result = []
    
    for query in queries:
        if query[0] == "?" and query[-1] == "?":
            try:
                result.append(len(list(chain(*get_word_dict(words)[len(query)][0].values()))))
            except KeyError:
                result.append(0)
        
        if query[0] == "?":
            try:
                words = word_dict[len(query)][1][query[-1]]
                result.append(search_lyric(words, query))
            except KeyError:
                result.append(0)
        else:
            try:
                words = word_dict[len(query)][0][query[0]]
                result.append(search_lyric(words, query))
            except KeyError:
                result.append(0)
    
    return result

# --- 네 번째 시도 ---
# 효율성 2개 실패

from collections import defaultdict

def get_word_dict(words):
    word_dict = defaultdict(list)
    
    for word in words:
        word_dict[len(word)].append(word)
    
    for value in word_dict.values():
        value.sort()
    
    return word_dict

def get_wildcard_idx(query):
    if query[0] == "?" and query[-1] == "?":
        return (0, len(query) - 1)
    
    start = 0
    end = len(query)
    
    if query[0] == "?":    
        while start <= end:
            mid = (start+end) // 2
            
            if mid == start:
                break
            
            if query[mid] == "?":
                start = mid
            else:
                end = mid
        
        return (0, mid)
    else:
        while start <= end:
            mid = (start+end) // 2
            
            if mid == start:
                break
            
            if query[mid] == "?":
                end = mid
            else:
                start = mid
        
        return (mid + 1, len(query) - 1)


def search_lyric(words, query):
        idx = get_wildcard_idx(query)
        
        if idx == (0, len(query) - 1):
            return len(words)
        
        if idx[0] == 0:
            query = query[idx[1] + 1:]

            return sum(1 for word in words if word.endswith(query))
        else:
            query = query[:idx[0]]
            
            return sum(1 for word in words if word.startswith(query))

def solution(words, queries):
    word_dict = get_word_dict(words)
    
    return [search_lyric(word_dict[len(query)], query) for query in queries]

# --- 다섯 번째 시도 ---
# 드디어 성공

from bisect import bisect_left, bisect_right
from collections import defaultdict

def get_word_dict(words):
    word_dict = defaultdict(list)
    
    for word in words:
        word_dict[len(word)].append(word)
    
    for key, value in word_dict.items():
        word_dict[key] = [sorted(value), sorted(v[::-1] for v in value)]
    
    return word_dict

def solution(words, queries):
    word_dict = get_word_dict(words)
    result = []
    
    for query in queries:
        words = word_dict[len(query)]
        
        if words:
            if query[-1] == "?":
                words = words[0]
                result.append(bisect_right(words, query.replace("?", "z")) - bisect_left(words, query.replace("?", "a")))
            else:
                words = words[1]
                result.append(bisect_right(words, query.replace("?", "z")[::-1]) - bisect_left(words, query.replace("?", "a")[::-1]))
        else:
            result.append(0)
    
    return result