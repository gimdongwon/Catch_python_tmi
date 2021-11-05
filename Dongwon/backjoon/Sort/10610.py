# # 1차 시도

# n = input()

# from itertools import permutations

# arr = list(permutations(list(n), len(n)))
# arr = sorted([int("".join(item)) for item in arr], reverse=True)

# for i in range(len(arr)):
#     if arr[i] % 30 == 0:
#         print(arr[i])
#         break
# else:
#     print(-1)

# 2차시도

# from itertools import permutations


# n = "".join(sorted(list(input())))
# thritys = list(map(int, [i * 30 for i in range(1, 33)]))
# print(n, "@@")
# print(thritys)
# if n not in thritys:
#     print(-1)
# else:
#     arr = list(permutations(list(n), len(n)))
#     arr = sorted([int("".join(item)) for item in arr],reverse=True)
    
#     for item in arr:
#         if item % 30 ==0:
#             print(item)
#             break
    
# 3차 시도

n = list(input())
n.sort(reverse=True)
result = 0

for i in n:
    result += int(i)
if result % 3 != 0 or "0" not in n:
    print(-1)
else:
    print("".join(n))