from common import proper_divisors

dp = {}

longest_chain = 0
longest_chain_start = None
for i in range(2, 1_000_000):
    if i in dp:
        continue

    dp[i] = True

    chain = [i]
    next  = sum(proper_divisors(i))
    while next not in dp and next < 1_000_000 and next != 0:
        dp[next] = True
        chain.append(next)
        # if next == 12496:
        #     print(chain)
        next = sum(proper_divisors(next))

    if next == i:
        if len(chain) > longest_chain:
            print(chain)
            longest_chain = len(chain)
            longest_chain_start = min(chain)
    elif next in chain:
        inext = chain.index(next)
        l = len(chain) - inext
        if l > longest_chain:
            print(chain[inext:])
            longest_chain = l
            longest_chain_start = next
    
    if i % 1000 == 0:
        print(i)

print(longest_chain)
print(longest_chain_start)
# print(proper_divisors(28))