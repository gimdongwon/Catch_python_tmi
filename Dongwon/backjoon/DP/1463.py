# import sys
# sys.setrecursionlimit(10**6)

# x = int(input())

# i = 0
# arr = []
# def cal(n, k):
#     if n == 1:
#         arr.append(k)
#         return
#     if n % 3 == 0:
#         cal(n // 3, k+1)
#     if n % 2 == 0:
#         cal(n // 2, k+1)
#     cal(n - 1, k+1)    

# cal(x,i)
# print(min(arr))

x = int(input())
arr = [0] * (x+1)

for i in range(2, x+1):
    arr[i] = arr[i-1] + 1
    if i % 3 == 0:
        arr[i] = min(arr[i], arr[i//3] + 1)
    if i % 2 == 0:
        arr[i] = min(arr[i], arr[i//2] + 1)
print(arr[x])