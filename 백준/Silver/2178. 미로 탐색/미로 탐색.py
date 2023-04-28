import sys


def check_valid_position(i, j, end_i, end_j):
    return i < 0 or j < 0 or i >= end_i or j >= end_j


def bfs(end_i, end_j):
    queue = []

    queue.append([0, 0])
    path_no[0][0] = 1
    while len(queue) > 0:
        position = queue.pop(0)

        for di, dj in direction:
            i = position[0]+di
            j = position[1]+dj
            if check_valid_position(i, j, end_i, end_j):
                continue

            if data[i][j] == '1' and path_no[i][j] == 0:
                path_no[i][j] = 1 + path_no[position[0]][position[1]]
                queue.append([i, j])


end_i, end_j = map(int, sys.stdin.readline().split())
data = []
for _ in range(end_i):
    data.append(list(sys.stdin.readline().rstrip()))

path_no = [[0 for _ in range(end_j)] for _ in range(end_i)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 오, 아, 왼, 위

bfs(end_i, end_j)
print(path_no[end_i-1][end_j-1])