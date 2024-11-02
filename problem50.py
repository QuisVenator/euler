import pyprimesieve


# This solution is stupid, it was late

primes = pyprimesieve.primes(10**6)

dp = {}
longest_sum = 1

def dp_sum(start, end):
    if (start,end) in dp:
        return dp[(start,end)]
    
    dp[(start,end)] = sum(primes[start:end])
    return dp[(start,end)]

def sliding_window_sum(prime, start, end):
    s = dp_sum(start, end)
    while True:
        if end - start < longest_sum:
            return 0
        
        if s == prime:
            return end - start
        elif s < prime:
            end += 1
            s += primes[end-1]
        else:
            start += 1
            s -= primes[start-1]


lprime = 0
for num, prime in enumerate(primes):
    s = sliding_window_sum(prime, 0, longest_sum)
    if s > longest_sum:
        longest_sum = s
        lprime = prime

    # print progress
    if num % 1000 == 0:
        print(f"{prime} - {num / len(primes) * 100:.2f}%")

print()
print(f"Longest sum: {longest_sum} - Prime: {lprime}")

