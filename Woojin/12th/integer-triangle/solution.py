# --- 백준 스타일 ---

n = int(input())
triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))
    
for i in reversed(range(n)):
    for j in range(i + 1):
        if i == n - 1:
            continue
        
        triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

print(triangle[0][0])