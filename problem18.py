import pandas as pd

triangle_str = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

triangle = [[int(num) for num in line.split()] for line in triangle_str.strip().split("\n")]

print(pd.DataFrame(triangle))

dp = {}
dp[(0, 0)] = triangle[0][0]
max_sum = dp[(0, 0)]

def max_path(i, j):   
    global max_sum
    global dp

    if (i, j) in dp:
        return dp[(i, j)]
    
    dp[(i, j)] = triangle[i][j]
    if i > 0:
        if j > 0:
            dp[(i, j)] += max_path(i - 1, j - 1)
        if j < i:
            dp[(i, j)] = max(dp[(i, j)], triangle[i][j] + max_path(i - 1, j))
    if dp[(i, j)] > max_sum:
        max_sum = dp[(i, j)]
    return dp[(i, j)]

for i in range(len(triangle[-1])):
    max_path(len(triangle) - 1, i)

print(max_sum)
