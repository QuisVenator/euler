coin_options = [1, 2, 5, 10, 20, 50, 100, 200]


dp = {}
def coin_sums(n, m):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if (n, m) in dp:
        return dp[n, m]
    
    dp[n, m] = 0
    for coin in coin_options:
        if coin <= m:
            dp[n, m] += coin_sums(n - coin, coin)
    
    return dp[n, m]

print(coin_sums(200, 200))