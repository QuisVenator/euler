dp = {}
dp[1] = 1

def next_term(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1
    
max_chain = 0
chain_starter = 1
def collatz(n):
    global max_chain
    global chain_starter
    if n in dp:
        return dp[n]
    else:
        dp[n] = 1 + collatz(next_term(n))
        if dp[n] > max_chain:
            max_chain = dp[n]
            chain_starter = n
        return dp[n]
    
for i in range(1, 1000000):
    collatz(i)
    print(f"i: {i}, dp[i]: {dp[i]}")

print(chain_starter)
print(max_chain)