import sys


def dfs(node, incidence_info: list, visited: list):
    visited[node] = True
    print(node, end=" ")
    for n in incidence_info[node]:
        if not visited[n]:
            dfs(n, incidence_info, visited)


def print_dfs(start_node, count_node, incidence_info):
    visited = [False] * (count_node+1)
    dfs(start_node, incidence_info, visited)


def bfs(node, incidence_info: list, visited: list):
    queue = []

    visited[node] = True
    queue.append(node)
    print(node, end=" ")
    while len(queue) > 0:
        n = queue.pop(0)
        for incidence_node in incidence_info[n]:
            if not visited[incidence_node]:
                visited[incidence_node] = True
                queue.append(incidence_node)
                print(incidence_node, end=" ")


def print_bfs(start_node, count_node, incidence_info):
    visited = [False] * (count_node+1)
    bfs(start_node, incidence_info, visited)


count_node, count_edge, start_node = map(int, sys.stdin.readline().split())
incidence_info = [[] for _ in range(count_node+1)]
for _ in range(count_edge):
    node1, node2 = map(int, sys.stdin.readline().split())
    incidence_info[node1].append(node2)
    incidence_info[node2].append(node1)

for node in range(1, count_node+1):
    incidence_info[node].sort()

print_dfs(start_node, count_node, incidence_info)
print()
print_bfs(start_node, count_node, incidence_info)
