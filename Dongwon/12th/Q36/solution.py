A,B = input().split(" ")
A,B = list(A), list(B)
result = 0
length = max(len(A), len(B))

dp = [0] * length

for i in range(length):
    if A[i] == B[i]:
        dp[i] = B[i]
        continue
    else:
        if A.count(A[i]) != B.count(A[i]):
            if len(A) > len(B):
                # 삭제
                A.remove(A[i])
            elif len(A)<len(B):
                # 추가
                A.insert(i, B[i])
            else:
                # 변경
                A[i] = B[i]
            dp[i] = B[i]
            result += 1
        
print(result, dp)