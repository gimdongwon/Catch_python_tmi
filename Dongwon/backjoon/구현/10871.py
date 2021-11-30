n,x = map(int, input().split())

arr = list(map(int, input().split()))

result = ""

for item in arr:
    if item < x:
        result += str(item) + " "

print(result.rstrip())