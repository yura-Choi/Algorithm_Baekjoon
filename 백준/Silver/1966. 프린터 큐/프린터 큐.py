import sys

T = int(sys.stdin.readline())
for _ in range(T):
    size, target = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    target_priority = arr[target]
    turn = 1

    while size > 0:
        if arr[0] != max(arr):
            arr.append(arr.pop(0))
        else:
            if target == 0:
                break
            arr.pop(0)
            size -= 1
            turn += 1
        target = (target - 1) % size

    print(turn)