from collections import defaultdict
# Counter, most_common 사용하기

word = input().lower()

s = set(word)

s_cnt = defaultdict(int)

for item in s:
    s_cnt[item] = word.count(item)

s_cnt_max = max(s_cnt.values())

result = list(filter(lambda x: x[1]==s_cnt_max, s_cnt.items()))

print(result[0][0].upper() if len(result)==1 else "?")