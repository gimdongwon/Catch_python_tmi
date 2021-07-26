# coding=utf-8
from bisect import bisect_left, bisect_right


# coding=utf-8
# 효율성 실패(시간 초과)
def solution(words, queries):
    result = []
    for query in queries:
        count = 0
        n = len(query)
        sorted_query = sorted(query)
        start = bisect_left(sorted_query, "?")
        end = bisect_right(sorted_query, "?")
        qu_mark = end - start
        for word in words:
            if query[0] != "?":
                if query[:n - qu_mark] == word[:n - qu_mark] and n == len(word):
                    count += 1
            else:
                if query[qu_mark:] == word[qu_mark:] and n == len(word):
                    count += 1
        result.append(count)

    return result


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
