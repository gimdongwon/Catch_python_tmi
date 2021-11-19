n = int(input())

words = [input() for _ in range(n)]
result = 0

for word in words:
    stack = []
    for i in range(len(word)):
        if len(stack) == 0:
            stack.append(word[i])
        else:
            if stack[-1] == word[i]:
                stack.pop()
            else:
                stack.append(word[i])
    if len(stack) == 0:
        result += 1
print(result)