import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    item = input().split()
    command = item[0]
    if command == 'push':
        stack.append(item[1])
    elif command =='pop':
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    elif command == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)