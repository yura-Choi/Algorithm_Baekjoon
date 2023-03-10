import sys


def bfs(start_i, start_j, group_id):
    queue = []

    queue.append([start_i, start_j])
    while len(queue) > 0:
        i, j = queue.pop(0)

        if i > 0 and ground[i-1][j] == 1:
            ground[i-1][j] = group_id
            queue.append([i-1, j])
        if j < col-1 and ground[i][j+1] == 1:
            ground[i][j+1] = group_id
            queue.append([i, j+1])
        if i < row-1 and ground[i+1][j] == 1:
            ground[i+1][j] = group_id
            queue.append([i+1, j])
        if j > 0 and ground[i][j-1] == 1:
            ground[i][j-1] = group_id
            queue.append([i, j-1])


T = int(sys.stdin.readline())
for _ in range(T):
    col, row, K = map(int, sys.stdin.readline().split())
    ground = [[0] * col for _ in range(row)]
    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split())
        ground[x][y] = 1

    # 0과 1이 이미 사용 중인 숫자 이므로 이를 피하기 위해 10번부터 시작
    group_id = 10
    for i in range(row):
        for j in range(col):
            if ground[i][j] == 1:
                bfs(i, j, group_id)
                group_id += 1

    print(group_id-10)

