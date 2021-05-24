n = int(input())

people = sorted(list(map(int, input().split())), reverse=False)
group = []
result = 0
for item in people:
    group.append(item)
    if group[-1] == len(group):
        group = []
        result += 1
    
print(result)