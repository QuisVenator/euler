import pyprimesieve
import math

primes = pyprimesieve.primes(math.floor(math.sqrt(600851475143)))

for i in reversed(primes):
    if 600851475143 % i == 0:
        print(i)
        break