x = int(input())
cache = [0] * x

for n in range(2, x+1):
    case = []
    if n % 3 == 0:
        case.append(1 + cache[(n//3)-1])
    if n % 2 == 0:
        case.append(1 + cache[(n//2)-1])
    case.append(1 + cache[(n-1)-1])
    
    cache[n-1] = min(case)

print(cache[x-1])