
dp = {}
def coin_sep(remaining, last_group):
    if remaining == 0:
        return 1
    if remaining < 0:
        return 0
    if last_group > remaining:
        return 0
    if (remaining, last_group) in dp:
        return dp[(remaining, last_group)]
    
    count = 0
    for i in range(last_group, remaining + 1):
        count += coin_sep(remaining - i, i)
    dp[(remaining, last_group)] = count
    return count

n = 1
while True:
    possible = coin_sep(n, 1)
    if possible % 1_000_000 == 0:
        print(n)
        break
    if n % 100 == 0:
        print(n, possible)
    n += 1