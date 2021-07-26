# --- 백준 스타일 ---

def get_2d(array, n, m):
    new_array = []
    
    for i in range(0, n * m, m):
        new_array.append(array[i:i + m])
    
    return new_array

def get_value(matrix, i, j):
    n, m = len(matrix), len(matrix[0])
    
    if 0 <= i < n and 0 <= j < m:
        return matrix[i][j]
    else:
        return 0

def get_max_gold(test_case):
    n, m = len(test_case), len(test_case[0])
    
    for j in range(m):
        for i in range(n):
            if j == 0:
                continue
            
            test_case[i][j] += max(
                get_value(test_case, i - 1, j - 1), 
                get_value(test_case, i, j - 1), 
                get_value(test_case, i + 1, j - 1)
                )
    
    return max(t[m - 1] for t in test_case) # print(max(list(zip(*test_case))[m - 1]))

T = int(input())
test_cases = []

for _ in range(T):
    n, m = map(int, input().split())
    test_case = list(map(int, input().split()))
    test_cases.append(get_2d(test_case, n, m))

for test_case in test_cases:
    print(get_max_gold(test_case))