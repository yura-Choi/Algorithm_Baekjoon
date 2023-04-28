def dq(N, i, j):
    global no

    if N == 0:
        return

    size = 2**N
    half_size = size // 2
    i_over = i >= half_size
    j_over = j >= half_size

    if not i_over and j_over:
        no += half_size**2
        j -= half_size
    elif i_over and not j_over:
        no += (half_size**2) * 2
        i -= half_size
    elif i_over and j_over:
        no += (half_size**2) * 3
        i -= half_size
        j -= half_size

    dq(N - 1, i, j)


N, r, c = map(int, input().split())
no = 0

dq(N, r, c)
print(no)
