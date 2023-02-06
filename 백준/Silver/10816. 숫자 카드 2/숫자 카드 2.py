import sys
from collections import Counter

N = int(sys.stdin.readline())
card_dict = Counter(sys.stdin.readline().split())

M = int(sys.stdin.readline())
card_num = sys.stdin.readline().split()
for num in card_num:
    if num in card_dict.keys():
        sys.stdout.write(str(card_dict[num])+' ')
    else:
        sys.stdout.write('0 ')
