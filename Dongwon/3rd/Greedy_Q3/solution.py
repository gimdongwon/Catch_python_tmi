S = input()

result = [S[0]]

for i in range(len(S)-1):
    if S[i] != S[i-1]:
        result.append(S[i])

print(len("".join(result))//2)