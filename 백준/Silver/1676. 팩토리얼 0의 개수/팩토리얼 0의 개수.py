import math

N = int(input())

factorial_N = str(math.factorial(N))
count = 0
for i in range(len(factorial_N)-1, -1, -1):
    if factorial_N[i] == '0':
        count += 1
    else:
        break
print(count)