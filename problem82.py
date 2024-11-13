from queue import PriorityQueue

with open("inputs/0082_matrix.txt") as f:
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

visited = [[False for _ in range(m)] for _ in range(n)]
weight_matrix = [[float("inf") for _ in range(m)] for _ in range(n)]

def bfs(x, y):
    q = PriorityQueue()
    q.put((matrix[x][y], x, y))
    visited[x][y] = True

    while not q.empty():
        value, x, y = q.get()
        # print(f"({x}, {y}) -> {value}")
        if y == m-1:
            return value

        # Move down
        if x+1 < n and not visited[x+1][y]:
            q.put((value + matrix[x+1][y], x+1, y))
            weight_matrix[x+1][y] = value + matrix[x+1][y]
            visited[x+1][y] = True

        # Move right
        if y+1 < m and not visited[x][y+1]:
            q.put((value + matrix[x][y+1], x, y+1))
            weight_matrix[x][y+1] = value + matrix[x][y+1]
            visited[x][y+1] = True

        # Move up
        if x-1 >= 0 and not visited[x-1][y]:
            q.put((value + matrix[x-1][y], x-1, y))
            weight_matrix[x-1][y] = value + matrix[x-1][y]
            visited[x-1][y] = True    


best_way = float("inf")
# print(bfs(1, 0))
# for row in weight_matrix:
#     print(row)
for i in range(n):
    option = bfs(i, 0)
    if option < best_way:
        best_way = option

    print(f"Option for {i}: {option}")
    
    # Reset visited
    visited = [[False for _ in range(m)] for _ in range(n)]


print(best_way)
