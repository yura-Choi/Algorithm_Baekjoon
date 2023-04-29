import sys

def dfs(N, start_node, node):
    for j in range(N):
        if matrix[node][j] == 1 and visited[j] == 0:
            visited[j] = 1
            matrix[start_node][j] = 1
            dfs(N, start_node, j)


N = int(sys.stdin.readline().rstrip())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    visited = [0] * N
    dfs(N, i, i)

for i in range(N):
    print(*matrix[i])
