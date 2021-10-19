alphabets = list("abcdefghijklmnopqrstuvwxyz")

word = input()

result = dict()

for alphabet in alphabets:
    result[alphabet] = 0

for i in word:
    result[i] += 1

print(" ".join(map(str, result.values())))