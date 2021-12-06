a,b = input().split()
result = []

for i in range(len(b) - len(a) + 1):
    temp = 0
    for j in range(len(a)):
        if a[j] != b[j+i]:
            temp += 1
    result.append(temp)

print(min(result))