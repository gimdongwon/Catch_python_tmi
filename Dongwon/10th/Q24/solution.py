N = int(input())
houses = list(map(int, input().split()))
houses.sort()
# 정렬 후 중간 값 출력
if len(houses)%2 == 1:
    print(houses[N//2])
else:
    print(houses[N//2 - 1])