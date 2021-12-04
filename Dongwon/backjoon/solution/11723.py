import sys
input = sys.stdin.readline

m = int(input())
result = set()

for _ in range(m):
    temp = input().split()
    command = temp[0]
    if len(temp) == 1:
        if command == 'all':
            result = set([i for i in range(1,21)])
        else:
            result = set()
    else:
        num = int(temp[1])
        if command == 'add' and 1<=num<=20:
            result.add(num)
        elif command == 'remove' and 1<=num<=20:
            result.discard(num)
        elif command == 'check' and 1<=num<=20:
            if num in result:
                print(1)
            else:
                print(0)
        elif command == 'toggle' and 1<=num<=20:
            if num in result:
                result.discard(num)
            else:
                result.add(num)
