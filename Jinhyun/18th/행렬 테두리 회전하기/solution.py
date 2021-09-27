def solution(rows, cols, queries):
    matrix = []
    for i in range(1, rows+1):
        matrix.append([(i-1) * cols + j for j in range(1, cols+1)])
    answer = []
    for query in queries :
        x1, y1, x2, y2 = [i - 1 for i in query]
        min_val = matrix[x1][y1]
        val = matrix[x1][y1]
        # 서쪽 올라가기
        for i in range(x1, x2) :
            min_val = min(matrix[i+1][y1], min_val)
            matrix[i][y1] = matrix[i+1][y1]
        # # 남쪽 왼쪽으로
        min_val = min(min(matrix[x2][y1 + 1 : y2 + 1]), min_val)
        matrix[x2][y1:y2] = matrix[x2][y1 + 1 : y2 + 1]
        # # 동쪽 아래로
        for j in range(x1, x2) :
            min_val = min(matrix[j][y2], min_val)
            matrix[j+1][y2] = matrix[j][y2]
        # # 북쪽 오른쪽으로
        min_val = min(min(matrix[x1][y1:y2]), min_val)
        matrix[x1][y1+1:y2+1] = matrix[x1][y1:y2]
        # # 값 복원
        matrix[x1][y1+1] = val
        answer.append(min_val)
    return answer