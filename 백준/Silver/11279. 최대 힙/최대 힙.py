import sys


def add_maxheap(heap, size, data):
    size += 1
    heap[size] = data

    # reorganize
    i = size
    while i > 1 and heap[i//2] < heap[i]:
        heap[i//2], heap[i] = heap[i], heap[i//2]
        i //= 2
    return size


def remove_maxheap(heap, size):
    item = heap[1]
    heap[1], heap[size] = heap[size], heap[1]
    heap[size] = 0
    size -= 1

    # reorganize
    i = 1
    while i*2 <= size:
        bigger = i*2
        if bigger+1 <= size and heap[bigger] < heap[bigger+1]:
            bigger = bigger+1

        if heap[i] >= heap[bigger]:
            break
        heap[i], heap[bigger] = heap[bigger], heap[i]
        i = bigger

    return item, size


N = int(sys.stdin.readline())
heap = [0] * (N+1)
size = 0

for _ in range(N):
    data = int(sys.stdin.readline())

    if data > 0:
        size = add_maxheap(heap, size, data)
    else:
        if size == 0:
            print(0)
        else:
            data, size = remove_maxheap(heap, size)
            print(data)