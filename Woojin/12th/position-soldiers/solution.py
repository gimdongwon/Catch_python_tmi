# --- 백준 스타일 ---

N = int(input())
soldiers = list(map(int, input().split()))
n_subseq = [1] * N

for i in range(N):
    for j in range(i):
        if soldiers[i] < soldiers[j]:
            n_subseq[i] = max(n_subseq[i], n_subseq[j] + 1)

print(N - max(n_subseq))