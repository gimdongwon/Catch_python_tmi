# --- 백준 스타일 ---

# --- 풀이 1 ---
# 못생긴 수를 미리 10000개 만들어서 n(1<=n<=1000)번째 못생긴 수를 인덱싱하는 풀이
# 못생긴 수에 2, 3, 5를 곱한 수도 못생긴 수라는 사실을 이용
# 중복으로 삽입되는 못생긴 수를 집합으로 처리함
# 예: numbers = {1} -> {2, 3, 5} -> {4, 6, 10, 6, 9, 15, 10, 15, 25} = {4, 6, 9, 10, 15, 25} -> ...

n = int(input())
ugly_numbers = {1}
numbers = {1}

while len(ugly_numbers) <= 10000:
    result = set()
    
    for x in numbers:
        for a in [2, 3, 5]:
            result.add(a * x)
    
    ugly_numbers = ugly_numbers | result
    numbers = result

ugly_numbers = sorted(ugly_numbers)
print(ugly_numbers[n - 1])

# --- 풀이 2 ---
# 못생긴 수 순서대로 찾는 방법

n = int(input())

ugly_numbers = [0] * n # 못생긴 수를 담기 위한 테이블 (1차원 DP 테이블)
ugly_numbers[0] = 1    # 첫 번째 못생긴 수는 1

i2 = i3 = i5 = 0              # 2, 3, 5를 곱하기 전의 결과값 인덱스
next2, next3, next5 = 2, 3, 5 # 2, 3, 5를 곱한 결과값

# n번째까지 못생긴 수들 찾기
for i in range(1, n):
    ugly_numbers[i] = min(next2, next3, next5)
        
    if ugly_numbers[i] == next2:
        i2 += 1
        next2 = ugly_numbers[i2] * 2
        
    if ugly_numbers[i] == next3:
        i3 += 1
        next3 = ugly_numbers[i3] * 3
        
    if ugly_numbers[i] == next5:
        i5 += 1
        next5 = ugly_numbers[i5] * 5

# n번째 못생긴 수 출력
print(ugly_numbers[n - 1])