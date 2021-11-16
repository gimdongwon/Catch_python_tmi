import sys
input = sys.stdin.readline

s = list(input().strip())
stack = []

k = int(input())

for _ in range(k):
    command = input().split()
    if command[0] == "L":
        if s:
            stack.append(s.pop())
    elif command[0] == "D":
        if stack:
            s.append(stack.pop())
    elif command[0] == "B":
        if s:
            s.pop()
    else:
        s.append(command[1])
    
print("".join(list(filter(lambda x: x!='\n', s)) + list(reversed(stack))))