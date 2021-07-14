# --- 백준 스타일 ---

N = int(input())
houses = sorted(map(int, input().split()))

print(houses[(len(houses)-1) // 2])