from collections import deque

N = int(input())
card_queue = deque([i for i in range(1, N+1)])
while len(card_queue) > 1:
    first = card_queue.popleft()
    card_queue.append(card_queue.popleft())
print(card_queue.pop())