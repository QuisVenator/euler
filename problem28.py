def spiral_diagonal_sum(n):
    if n == 1:
        return 1
    # return n**2 + n**2 - n + 1 + n**2 - 2 * n + 2 + n**2 - 3 * n + 3 + spiral_diagonal_sum(n - 2)
    return 4*n**2 - 6*n + 6 + spiral_diagonal_sum(n - 2)

print(spiral_diagonal_sum(1001))