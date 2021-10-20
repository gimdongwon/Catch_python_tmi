s = input().split("-")

for i in range(len(s)):
    if "+" in s[i]:
        s[i] = sum(map(int, s[i].split("+")))
    else:
        s[i] = int(s[i])

result = s[0]
for i in range(1, len(s)):
    result -= s[i]
print(result)