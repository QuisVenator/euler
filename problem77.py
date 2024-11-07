import pyprimesieve

primes = pyprimesieve.primes(1000)

dp = {}

def prime_sum(remaining, last_i):
    global primes

    if remaining == 0:
        return 1
    if remaining < 0:
        return 0
    if primes[last_i] > remaining:
        return 0
    if (remaining, last_i) in dp:
        return dp[(remaining, last_i)]
    
    count = 0
    for i in range(last_i, len(primes)):
        count += prime_sum(remaining - primes[i], i)
    
    dp[(remaining, last_i)] = count
    return count

i = 1
while True:
    possible = prime_sum(i, 0)
    if possible > 5000:
        print(i)
        break
    print(i, possible)
    i += 1
