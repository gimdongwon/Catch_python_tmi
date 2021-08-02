# coding=tf-8

# 첫번째 풀이(오답)
# 에토스테네스의 체
# 소수 개수 구하기
def count_prime_and_seven(n):
    a = [False, False] + [True] * (n - 1)
    primes = []

    print (a)

    for i in range(2, n + 1):
        if a[i] or i % 7 == 0:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False

    print(primes)
    print (a)

    return len(primes)


def solution(n):
    # 7의 배수와 소수 제외
    primes = count_prime_and_seven(n)
    num = 1
    while num == 0:
        num = count_prime_and_seven(n)
        n = n + num
    return n + primes


print (solution(10))


# 두번째 풀이
def solution2(n):
    cnt = 1
    num = 2
    while cnt < n:
        print (cnt, num)
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:  # 2또는 3또는 5의 배수이고
            if num % 7 != 0:  # 7의 배수가 아니면
                cnt += 1  # 못생긴 수
        num += 1
    return num - 1


print (solution2(4))
