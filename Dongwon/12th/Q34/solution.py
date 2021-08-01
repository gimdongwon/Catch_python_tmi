n = int(input())
arr = list(map(int, input().split(" ")))
arr.reverse() # 가장 긴 증가하는 수열로 바꾸어서 풀기 위해 reverse

dp = [1] * n #  최소 1의 길이는 가지므로 1로 초기화

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]: # i가 뒤에 수, j가 앞에 수 이므로 증가하는 형태
            dp[i] = max(dp[i], dp[j]+1) # 최대 값을 설정할 필요가 있고 j는 현재보다 증가해야 하므로 1추가.
print(dp)