# --- 백준 스타일 ---

A = input()
B = input()

col_names = [""] + list(A)
row_names = [""] + list(B)

n, m = len(row_names), len(col_names)

dist_tb = [[0] * m for _ in range(n)]
dist_tb[0] = list(range(m))

for i in range(n):
    dist_tb[i][0] = i

for i in range(1, n):
    for j in range(1, m):
        if row_names[i] == col_names[j]:
            dist_tb[i][j] = dist_tb[i - 1][j - 1]
        else:
            dist_tb[i][j] = 1 + min(dist_tb[i - 1][j - 1], dist_tb[i - 1][j], dist_tb[i][j - 1])

print(dist_tb[n - 1][m - 1])