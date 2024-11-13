

with open("inputs/0081_matrix.txt") as f:
    matrix = f.readlines()

# Matrix from example:
# matrix = [
#     "131,673,234,103,18",
#     "201,96,342,965,150",
#     "630,803,746,422,111",
#     "537,699,497,121,956",
#     "805,732,524,37,331"
# ]

matrix = [x.strip() for x in matrix]
for i in range(len(matrix)):
    matrix[i] = [int(x) for x in matrix[i].split(",")]

n = len(matrix)
m = len(matrix[0])

# looks good
# print(matrix)
# print(n)
# print(m)

# all values are >= 1
# smallest_value = 1000000
# for row in matrix:
#     for value in row:
#         if value < smallest_value:
#             smallest_value = value
# print(smallest_value)

dp = [[0 for _ in range(m)] for _ in range(n)]

dp[0][0] = matrix[0][0]

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + matrix[i][0]

for j in range(1, m):
    dp[0][j] = dp[0][j-1] + matrix[0][j]


for row in dp:
    print(row)

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i][j]

for row in dp:
    print(row)

print(dp[n-1][m-1])