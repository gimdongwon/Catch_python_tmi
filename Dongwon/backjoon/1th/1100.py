result = 0

board = []

for _ in range(8):
    board.append(list(input()))

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0 and board[i][j]=="F":
            result+=1

print(result)