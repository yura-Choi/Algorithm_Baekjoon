import sys

N = int(sys.stdin.readline())
db = []
for i in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    db.append([weight, height, 1])

for target in range(N):
    for i in range(N):
        if target == i:
            continue
        if db[target][0] < db[i][0] and db[target][1] < db[i][1]:
            db[target][2] += 1

print(' '.join([str(x[2]) for x in db]))