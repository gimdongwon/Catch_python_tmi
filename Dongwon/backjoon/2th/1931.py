n = int(input())

result = []

for i in range(n):
    s,e = map(int, input().split())
    result.append([s,e])

result.sort(key=lambda x: [x[1],x[0]])

answer = 1
end_time = result[0][1]

for i in range(1,n):
    if result[i][0] >= end_time:
        answer += 1
        end_time = result[i][1]

print(answer)