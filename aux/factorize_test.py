import pyprimesieve
import time
import argparse

parser = argparse.ArgumentParser(description="Test factorization methods")
parser.add_argument("test", type=int, help="Test to run")
# Add optional argument for numbers to test
parser.add_argument("--number", type=int, default=100_000, help="Number of integers to factorize,starting with one")
args = parser.parse_args()
test = args.test
num = args.number


def list_factors_with_sieve(n, primes):
    factors = []
    for prime in primes:
        if prime > n:
            break
        if n % prime == 0:
            factors.append(prime)
    return factors

dp = {}
def factorize_with_sieve(n, primes):
    factors = []
    for prime in primes:
        if n in dp:
            factors.extend(dp[n])
            break
        if prime > n:
            break
        exponent = 1
        while n % prime == 0:
            n //= prime
            exponent += 1
        factors.append((prime, exponent))
    
    dp[n] = factors
    return factors

def factorize_library(n):
    return pyprimesieve.factorize(n)

def list_factors_library(n):
    return [prime for prime, exponent in pyprimesieve.factorize(n)]

print("With default parameters, tests may take a few minutes to complete.")
if test == 1:
    print("Testing full factorization with primelist")
    start_with_sieve = time.process_time()

    primes = pyprimesieve.primes(10**6)

    start_no_sieve = time.process_time()

    for i in range(num):
        factorize_with_sieve(i, primes)
    
    stop = time.process_time()
    print(f"Time to generate primes: {start_no_sieve - start_with_sieve}")
    print(f"Time including generating primes: {stop - start_with_sieve}")
    print(f"Time excluding generating primes: {stop - start_no_sieve}")

if test == 2:
    print("Testing factor listing with primelist")
    start_with_sieve = time.process_time()

    primes = pyprimesieve.primes(10**6)

    start_no_sieve = time.process_time()

    for i in range(num):
        list_factors_with_sieve(i, primes)
    
    stop = time.process_time()
    print(f"Time to generate primes: {start_no_sieve - start_with_sieve}")
    print(f"Time including generating primes: {stop - start_with_sieve}")
    print(f"Time excluding generating primes: {stop - start_no_sieve}")

if test == 3:
    print("Testing full factorization with library")
    start = time.process_time()

    for i in range(num):
        factorize_library(i)
    
    stop = time.process_time()
    print(f"Time including generating primes: {stop - start}")

if test == 4:
    print("Testing factor listing with library")
    start = time.process_time()

    for i in range(num):
        list_factors_library(i)
    
    stop = time.process_time()
    print(f"Time including generating primes: {stop - start}")
