import math

N = int(input())

factorial_N = str(math.factorial(N))[::-1]

count = 0
for e in factorial_N:
    if e == '0':
        count += 1
    else:
        break
print(count)