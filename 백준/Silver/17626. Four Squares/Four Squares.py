from math import sqrt, pow


# n == (4**a)(8b+7)
def squares_4(n):
    while n % 4 == 0:
        n //= 4
    return n % 8 == 7


def squares_2(n):
    sqrt_num = int(sqrt(N))
    for x in range(sqrt_num, 0, -1):
        x1 = pow(x, 2)
        x2 = pow(int(sqrt(N - x1)), 2)
        if x1 + x2 == N:
            return True
    return False


def squares_1(n):
    return pow(int(sqrt(n)), 2) == N


N = int(input())
result = 0

# 1
if squares_1(N):
    result = 1

# 4
if result == 0 and squares_4(N):
    result = 4

# 2
if result == 0 and squares_2(N):
    result = 2

# 3
if result == 0:
    result = 3

print(result)
