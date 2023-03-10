import sys
sys.setrecursionlimit(10000)

def check_paper(start_i, start_j, n):
    target = paper[start_i][start_j]
    for i in range(n):
        for j in range(n):
            if paper[start_i+i][start_j+j] != target:
                return -2
    return target


def count_paper(start_i, start_j, n):
    result = check_paper(start_i, start_j, n)
    if result != -2:
        paper_type[result+1] += 1
    else:
        size = n // 3
        row = start_i
        while row < start_i + n:
            col = start_j
            while col < start_j + n:
                count_paper(row, col, size)
                col += size
            row += size


N = int(sys.stdin.readline())
paper = []
paper_type = [0, 0, 0]

for i in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

count_paper(0, 0, N)
print(*paper_type)