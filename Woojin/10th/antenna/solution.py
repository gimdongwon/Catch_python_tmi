# --- 백준 스타일 ---

N = int(input())
houses = list(map(int, input().split()))
houses.sort()
h_len = len(houses)

if h_len % 2:
    print(houses[h_len // 2])
else:
    print(houses[h_len//2 - 1])