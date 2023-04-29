import sys


def bfs(start_node, N):
    queue = []
    visited = [0] * N

    queue.append(start_node)
    # don't check start_node's visited value
    while len(queue) > 0:
        n = queue.pop(0)
        for j in range(N):
            if matrix[n][j] == 1 and visited[j] == 0:
                queue.append(j)
                visited[j] = 1
                matrix[start_node][j] = 1


N = int(sys.stdin.readline().rstrip())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    bfs(i, N)

for i in range(N):
    for j in range(N):
        print(matrix[i][j], end=" ")
    print()
