from collections import deque

N, K = map(int, input().split())
queue = deque([str(x) for x in range(1, N+1)])
result = []

while N > 0:
    for i in range(K-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())
    N -= 1
print(f"<{', '.join(result)}>")