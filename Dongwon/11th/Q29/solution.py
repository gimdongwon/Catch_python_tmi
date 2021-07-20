N,C = map(int, input().split())

houses = [int(input()) for _ in range(N)]

houses.sort()

answer = 0
start, end = 1, houses[-1] - houses[0]

while start <= end:
    mid = (start + end) // 2
    wifis = 1 # 공유기 맨처음거 설치하고 시작
    start_house = houses[0] # 처음 시작 위치

    # 거리 비교
    for i in range(1,N):
        # 두 공유기 사이 거리를 이전보다 크게 설치 가능한 경우
        if start_house + mid <= houses[i]:
            # 공유기 설치
            wifis += 1
            # 시작 집 조정
            start_house = houses[i]
    
    if wifis >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)