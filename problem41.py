import pyprimesieve

# get primes with 9 digits or less
primes = pyprimesieve.primes(10**9)

def is_pandigital(n):
    n = str(n)
    for i in range(1, len(n) + 1):
        if str(i) not in n:
            return False
    return True
        
for i, prime in enumerate(reversed(primes)):
    if is_pandigital(prime):
        print(prime)
        break

    if i % 1000 == 0:
        print(f"{i / len(primes) * 100:.0f}%", end="\r")


