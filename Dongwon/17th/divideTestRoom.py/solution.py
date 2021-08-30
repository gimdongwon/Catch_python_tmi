left = [0] * 10005
right = [0] * 10005
x = [0] * 10005
p = [-1] * 10005
root = 0
cnt = 0
    
    # 현재 노드, 그룹의 최대 인원수
def dfs (cur, lim):
    global cnt
    lv = 0
    if left[cur] != -1:
        lv = dfs(left[cur], lim)
    rv = 0
    if right[cur] != -1:
        rv = dfs(right[cur], lim)
    if x[cur] + lv + rv <= lim:
        return x[cur] + lv + rv
    if x[cur] + min(lv, rv) <= lim:
        cnt += 1
        return x[cur] + min(lv,rv)
    cnt += 2
    return x[cur]

def solve(lim):
    global cnt
    cnt = 0
    dfs(root, lim)
    cnt += 1
    return cnt

def solution(k, num, links):
    global cnt
    n = len(num)
    for i in range(n):
        left[i], right[i] = links[i]
        x[i] = num[i]
        if left[i] != -1: p[left[i]] = i
        if right[i] != -1: p[right[i]] = i
    for i in range(n):
        if p[i] == -1:
            root = i
            break
    st = max(x)
    en = 10 ** 8
    
    while st < en:
        mid = (st+en) // 2
        if solve(mid) <= k:
            en = mid
        else:
            st = mid+1
    return st