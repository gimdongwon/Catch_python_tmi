def calculate(s):
    numbers = list(map(int, s))
    result = numbers[0]
    for i in range(1, len(numbers)):
        if result * numbers[i] == 0 or result * numbers[i] == result:
            result += numbers[i]
        else:
            result *= numbers[i]

    return result


print(calculate("02984"))

