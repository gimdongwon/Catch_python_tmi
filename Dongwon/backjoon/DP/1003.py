# t = int(input())


# for _ in range(t):
#     x = int(input())
#     zero_cnt, one_cnt = 0,0
#     def fibonacci(n):
#         global zero_cnt, one_cnt
#         if n == 0:
#             zero_cnt += 1
#             return 0
#         elif n == 1:
#             one_cnt += 1
#             return 1
#         else:
#             return fibonacci(n-1) + fibonacci(n-2)
#     fibonacci(x)
#     print(zero_cnt, one_cnt)

t = int(input())

zero,one = [1,0,1],[0,1,1]
for _ in range(t):
    x = int(input())
    def fibonacci(n):
        length = len(zero)
        if n >= length:
            for i in range(length, n+1):
                zero.append(zero[i-1] + zero[i-2])
                one.append(one[i-1] + one[i-2])
        print(zero[n], one[n])
    fibonacci(x)