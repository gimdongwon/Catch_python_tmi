# --- 백준 스타일 ---

def get_2d(array, n, m):
    new_array = []
    
    for i in range(0, n * m, m):
        new_array.append(array[i:i + m])
    
    return new_array

def get_value(matrix, i, j):
    try:
        return matrix[i][j]
    except IndexError:
        return 0

def get_max_gold(test_case):
    n, m = len(test_case), len(test_case[0])
    
    for j in reversed(range(m)):
        for i in range(n):
            if j == m - 1:
                continue
            
            test_case[i][j] += max(get_value(test_case, i - 1, j + 1), get_value(test_case, i, j + 1), get_value(test_case, i + 1, j + 1))
    
    return max(t[0] for t in test_case)

T = int(input())
test_cases = []

for _ in range(2 * T):
    n, m = map(int, input().split())
    test_case = list(map(int, input().split()))
    test_cases.append(get_2d(test_case, n, m))

for test_case in test_cases:
    print(get_max_gold(test_case))