n = int(input())

people = sorted(list(map(int, input().split())), reverse=True)
group = []
result = 0
for item in people:
    group.append(item)
    if max(group) == len(group):
        group = []
        result += 1
    
print(result)