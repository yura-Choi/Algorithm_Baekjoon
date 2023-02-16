import sys

cache = [0] * 12

# return (1, 2, 3을 이용하여 n을 표현하는 방법의 수)
def count_case(num):
    global cache

    # base case
    if num < 0:
        return 0
    elif num <= 1:
        return 1

    # memoization
    if cache[num] != 0:
        return cache[num]

    count = count_case(num-1) + count_case(num-2) + count_case(num-3)
    cache[num] = count
    return count


T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(count_case(n))