import sys

saved_num, find_num = map(int, sys.stdin.readline().split())
sites = {}
for _ in range(saved_num):
    site_name, password = sys.stdin.readline().split()
    sites[site_name] = password

result = ""
for _ in range(find_num):
    find_name = sys.stdin.readline().rstrip()
    result += sites[find_name]+"\n"
print(result)