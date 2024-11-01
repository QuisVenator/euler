dp = {}
dp[(20, 20)] = 1

def move(i, j):
    if (i, j) in dp:
        return dp[(i, j)]
    
    dp[(i, j)] = 0
    if i < 20:
        dp[(i,j)] += move(i + 1, j)
    if j < 20:
        dp[(i,j)] += move(i, j + 1)
    
    return dp[(i, j)]

print(move(0, 0))
