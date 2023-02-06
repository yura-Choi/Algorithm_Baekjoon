import sys

def binary_search(arr: list, start: int, end: int, n: int) -> bool:
    if start > end:
        return False

    mid = (start + end)//2
    if n == arr[mid]:
        return True
    elif n < arr[mid]:
        return binary_search(arr, start, mid-1, n)
    else:
        return binary_search(arr, mid+1, end, n)


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

arr.sort()
for n in num:
    if binary_search(arr, 0, N-1, n):
        print(1)
    else:
        print(0)