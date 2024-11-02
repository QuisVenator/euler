import pyprimesieve

primes = pyprimesieve.primes(1000000)
primes_set = set(primes)

circle_primes = set()


def is_circle_prime(n):
    n_str = str(n)
    for i in range(len(n_str)):
        if int(n_str[i:] + n_str[:i]) not in primes_set:
            return False
    return True


for i, prime in enumerate(primes):
    if prime in circle_primes:
        continue
    if is_circle_prime(prime):
        # Add all rotations of the prime
        n_str = str(prime)
        for i in range(len(n_str)):
            circle_primes.add(int(n_str[i:] + n_str[:i]))

    print(f"Progress: {i}/{len(primes)} ({i / len(primes) * 100:.2f}%)", end="\r")

print()
print(len(circle_primes))
        