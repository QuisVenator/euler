import pyprimesieve

primes = pyprimesieve.primes(10**4)
permutation_primes = {}

for prime in primes:
    prime_str = ''.join(sorted(str(prime)))
    if prime_str not in permutation_primes:
        permutation_primes[prime_str] = []
    permutation_primes[prime_str].append(prime)

for prime_str, prime_list in permutation_primes.items():
    if len(prime_list) < 3:
        continue

    for i in range(len(prime_list) - 2):
        for j in range(i + 1, len(prime_list) - 1):
            for k in range(j + 1, len(prime_list)):
                if prime_list[k] - prime_list[j] == prime_list[j] - prime_list[i]:
                    print(prime_list[i], prime_list[j], prime_list[k])