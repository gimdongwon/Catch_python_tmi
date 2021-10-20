import sys
input = sys.stdin.readline
n,m = map(int, input().split())

no_hear, no_see = set(), set()

for _ in range(n):
    no_hear.add(input().rstrip())

for _ in range(m):
    target = input().rstrip()
    no_see.add(target)

result = sorted(list(no_see & no_hear))

print(len(result))

for item in result:
    print(item)