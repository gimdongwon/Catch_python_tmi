from itertools import  permutations

n = int(input())
arr = list(map(int, input().split()))

arr = permutations(arr)
result = 0
for item in arr:
    temp = 0
    for j in range(len(item)-1):
        temp += abs(item[j] - item[j+1])
    result = max(result, temp)
print(result)

# 8 20 1 15 4 10