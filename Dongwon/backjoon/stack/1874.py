n = int(input())

stack = []
result = []
answer = []
graph = [int(input()) for _ in range(n)]

j = 0
for i in range(1,n+1):
    stack.append(i)
    answer.append("+")
    while stack and stack[-1] == graph[j]:
        answer.append("-")
        result.append(stack.pop())
        j+=1

if stack:
    print("NO")
else:
    for item in answer:
        print(item)