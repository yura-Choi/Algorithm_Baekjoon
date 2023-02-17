import sys


def DFS(node_num: int) -> int:
    is_visited[node_num-1] = 1
    count = 0
    for node in adjacency_list[node_num]:
        if is_visited[node-1] == 0:
            count += DFS(node)
    return count + 1


count_node = int(sys.stdin.readline())
count_edge = int(sys.stdin.readline())
adjacency_list = {}
for node in range(1, count_node+1):
    adjacency_list[node] = []

for _ in range(count_edge):
    node1, node2 = map(int, sys.stdin.readline().split())
    adjacency_list[node1].append(node2)
    adjacency_list[node2].append(node1)

is_visited = [0 for _ in range(count_node)]
print(DFS(1)-1)