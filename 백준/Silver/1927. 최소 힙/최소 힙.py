import sys


def add_minheap(heap, size, data):
    size += 1
    heap[size] = data

    i = size
    while i > 1 and heap[i//2] > heap[i]:
        heap[i//2], heap[i] = heap[i], heap[i//2]
        i //= 2
    return size


def remove_minheap(heap, size):
    item = heap[1]
    heap[1], heap[size] = heap[size], heap[1]
    heap[size] = 0
    size -= 1

    # reorganize
    i = 1
    while i*2 <= size:
        smaller = i*2
        if smaller+1 <= size and heap[smaller] > heap[i*2+1]:
            smaller = i*2+1

        if heap[i] < heap[smaller]:
            break
        heap[i], heap[smaller] = heap[smaller], heap[i]
        i = smaller

    return item, size


N = int(sys.stdin.readline())
heap = [0] * (N+1)
size = 0
for _ in range(N):

    data = int(sys.stdin.readline())
    if data > 0:
        size = add_minheap(heap, size, data)
    else:
        if size == 0:
            print(0)
        else:
            data, size = remove_minheap(heap, size)
            print(data)