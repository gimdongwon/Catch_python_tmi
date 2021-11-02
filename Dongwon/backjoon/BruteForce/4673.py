# 실버 5
result = [i for i in range(1, 10000)]
for i in range(1, 10000):
    if i + sum(list(map(int, list(str(i))))) in result:
        result.remove(i + sum(list(map(int, list(str(i))))))

for item in result:
    print(item)