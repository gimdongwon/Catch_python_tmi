S = input()

result = [S[0]]

for i in range(1, len(S)):
    if S[i] != S[i-1]:
        result.append(S[i])

print(result)
print(len("".join(result))//2)