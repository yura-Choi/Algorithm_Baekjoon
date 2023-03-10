import sys


def bfs(node: int, incidence_info: list):
    queue = []

    visited[node] = 1
    queue.append(node)
    while len(queue) > 0:
        n = queue.pop(0)
        n_list = incidence_info[n]
        for incidence_node in n_list:
            if visited[incidence_node] == 0:
                queue.append(incidence_node)
                visited[incidence_node] = 1


count_node, count_edge = map(int, sys.stdin.readline().split())
incidence_info = [[] for _ in range(count_node+1)]
visited = [0] * (count_node+1)

for _ in range(count_edge):
    node1, node2 = map(int, sys.stdin.readline().split())
    incidence_info[node1].append(node2)
    incidence_info[node2].append(node1)

count = 0
for node in range(1, count_node+1):
    if visited[node] == 0:
        bfs(node, incidence_info)
        count += 1
print(count)