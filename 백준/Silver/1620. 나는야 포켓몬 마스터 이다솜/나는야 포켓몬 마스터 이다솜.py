import sys


count_pocketmon, count_question = map(int, sys.stdin.readline().split())
name_to_num = {}
num_to_name = {}

for i in range(1, count_pocketmon+1):
    name = sys.stdin.readline().rstrip()
    name_to_num[name] = i
    num_to_name[str(i)] = name

for _ in range(count_question):
    question = sys.stdin.readline().rstrip()
    if question.isalpha():
        print(name_to_num[question])
    else:
        print(num_to_name[question])