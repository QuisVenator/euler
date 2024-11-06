from math import sqrt

dp = {}
perfect_squares = {}
for i in range(1, 1_500_000//2):
    perfect_squares[i**2] = i

squares = []

for i in range(1, 1_500_000//2):
    squares.append(i**2)

    for j, square in enumerate(squares):
        if i + j+1 > 1_500_000//2:
            break
        res = squares[-1] + square
        if res in perfect_squares:
            wire_len = i + j+1 + perfect_squares[res]
            if wire_len < 1_500_000:
                # print(wire_len, i, j, int(res), res)
                if wire_len not in dp:
                    dp[wire_len] = []
                dp[wire_len].append((wire_len, i, j+1, perfect_squares[res]))
    
    if i % 1000 == 0:
        print(i)

count = 0
for k, v in dp.items():
    if len(v) == 1:
        # print(k, v)
        count += 1
    # if len(v) > 1:
    #     print(k, v)

print(count)