n = int(input())
answer = 0
def remove_repeat(s):
    result = s[:]
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            result.remove(s[i])
    return result

for _ in range(n):
    word = list(input())
    word = remove_repeat(word)
    for i in range(len(word)):
        if word.index(word[i]) != i:
            break
    else:
        answer += 1
print(answer)