import sys

count_listen, count_see = map(int, sys.stdin.readline().split())
set_listen = set()
set_see = set()
for _ in range(count_listen):
    set_listen.add(sys.stdin.readline().rstrip())
for _ in range(count_see):
    set_see.add(sys.stdin.readline().rstrip())

intersect_name = list(set_listen.intersection(set_see))
print(len(intersect_name))
print('\n'.join(sorted(intersect_name)))
