import sys

def check_area(start_i, start_j) -> int:
    global board, start_color
    count = 0
    for i in range(start_i, start_i+8):
        for j in range(start_j, start_j+8):
            if (i + j) % 2 == 0:
                if board[i][j] != start_color: # 조건 불만족
                    count += 1
            else:
                if board[i][j] == start_color: # 조건 불만족
                    count += 1
    return count


row, col = map(int, sys.stdin.readline().split())
board = []
for i in range(row):
    board.append(list(sys.stdin.readline().strip()))

count_min = 65
start_color = 'B'
for i in range(row-7):
    for j in range(col-7):
        result = check_area(i, j)
        if result < count_min:
            count_min = result

start_color = 'W'
for i in range(row-7):
    for j in range(col-7):
        result = check_area(i, j)
        if result < count_min:
            count_min = result

print(count_min)
