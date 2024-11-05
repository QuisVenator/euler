# from common import phi
import pyprimesieve

primes = pyprimesieve.primes(10**7)


def phi(n):
    count = n
    factors = pyprimesieve.factorize(n)
    for factor, _ in factors:
        count *= (1 - 1/factor)
    
    return int(count)

min_phi_over_n = 10**7
min_n = 0

for n in range(2, 10**7):
    phi_n = phi(n)
    if sorted(str(n)) == sorted(str(phi_n)):
        ratio = n / phi_n
        if ratio < min_phi_over_n:
            min_phi_over_n = ratio
            min_n = n

    print(n, end='\r')
print()

print(min_n)
