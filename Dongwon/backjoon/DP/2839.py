n = int(input())

bag = 0

init_5 = n // 5
i = 0
while True:
    while n > (init_5 * 5) + (i * 3):
        i += 1
    if n == (init_5 * 5) + (i * 3):
        break
    init_5 -= 1
    i = 0
    if init_5 == -1:
        break

print(init_5 + i)