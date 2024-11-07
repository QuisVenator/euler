import sys
# sys.set_int_max_str_digits(100_000)
# dp = {}
# def coin_sep(remaining, last_group):
#     if remaining == 0:
#         return 1
#     if remaining < 0:
#         return 0
#     if last_group > remaining:
#         return 0
#     if (remaining, last_group) in dp:
#         return dp[(remaining, last_group)]
    
#     count = 0
#     for i in range(last_group, remaining + 1):
#         count += coin_sep(remaining - i, i)
#     dp[(remaining, last_group)] = count
#     return count

# n = 1
# while True:
#     possible = coin_sep(n, 1)
#     # print(n, possible)
#     if possible % 1_000_000 == 0:
#         print(n)
#         break
#     if n % 100 == 0:
#         print(n, possible)
        
#     n += 1


pentagonals = []
sign_for_partition = []
for i in range(1, 1000_000):
    pentagonals.append(i * (3 * i - 1) // 2)
    pentagonals.append(-i * (3 * -i - 1) // 2)
    sign_for_partition.append(-1 if i % 2 == 0 else 1)
    sign_for_partition.append(-1 if i % 2 == 0 else 1)

dp = {}
dp[0] = 1

def partition(n):
    if n < 0:
        return 0
    
    if n in dp:
        return dp[n]
    
    partition_sum = 0
    for i, p in enumerate(pentagonals):
        if p > n:
            break
        partition_sum += sign_for_partition[i] * partition(n - p)
    
    dp[n] = partition_sum
    return partition_sum

n = 1
while True:
    p = partition(n)
    # print(p)
    if p % 1_000_000 == 0:
        print(n)
        break
    n += 1
