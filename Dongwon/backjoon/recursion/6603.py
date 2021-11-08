# from itertools import combinations

# while True:
#     test = input()
#     if test == '0':
#         break
#     temp = list(map(int, test.split()))
#     k = temp[0]
#     arr = temp[1:]
#     for item in list(combinations(arr, 6)):
#         for jtem in item:
#             print(jtem, end=' ')
#         print()
#     print()
#     test = '0'

combi = [0 for _ in range(6)]

def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=' ')
        print()
        return
    for i in range(start, len(s)):
        combi[depth] = s[i]
        dfs(i+1, depth+1)
while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    del s[0]
    dfs(0,0)
    print()