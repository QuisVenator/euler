from math import sqrt

def resolve(n):
    dp = {}
    perfect_squares = {}
    for i in range(1, n//2):
        perfect_squares[i**2] = i

    squares = []

    for i in range(1, n//2):
        squares.append(i**2)

        for j, square in enumerate(squares):
            res = squares[-1] + square
            if i + j+1 + sqrt(res) > n:
                break
            if res in perfect_squares:
                wire_len = i + j+1 + perfect_squares[res]
                if wire_len < n:
                    # print(wire_len, i, j, int(res), res)
                    if wire_len not in dp:
                        dp[wire_len] = []
                    dp[wire_len].append((wire_len, i, j+1, perfect_squares[res]))
        
        if i % 1000 == 0:
            print(i)
    return dp

count = 0
dp = resolve(10_000)
# dp = resolve(1_500_000)
# for k, v in dp.items():
#     if len(v) == 1:
#         # print(k, v)
#         count += 1
#     # if len(v) > 1:
#     #     print(k, v)

# print(count)