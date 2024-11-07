
dp = {}

def solve(remaining, last):
    if remaining == 0:
        return 1
    if remaining < 0:
        return 0
    if last > remaining:
        return 0
    
    if (remaining, last) in dp:
        return dp[(remaining, last)]
    
    count = 0
    for i in range(last, remaining + 1):
        count += solve(remaining - i, i)
    
    dp[(remaining, last)] = count
    return count

print(solve(100, 1) - 1) # -1 because we don't want to count 100 itself