primes = [2,3,5,7,11,13,17,19]

def is_prime(n):
    for p in primes:
        if n % p == 0:
            return False
    return True

candidate = 21
while len(primes) < 10001:
    candidate = primes[-1] + 2
    while not is_prime(candidate):
        candidate += 2
    primes.append(candidate)

print(primes[-1])