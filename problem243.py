# We want to minimize phi(n)/(n-1)
# For simplicity, we can see that this should be the same as minimizing phi(n)/n
# We can see that phi(n) = n * (1 - 1/factor1) * (1 - 1/factor2) * ... * (1 - 1/factorN) where factorN are the prime factors of n
# Therefore, to minimize phi(n) we want to maximize the number of factors of n, as every factor will reduce the result, but the exonents dont
# So, we can get an initial result by just multplying a bunch of primes each with exponent 1
# We will call this selected_primes

from common import phi
import pyprimesieve

primes = pyprimesieve.primes(100)

def resilience(d):
    return phi(d), d - 1, phi(d) / (d - 1)

selected_primes = []
n = 1
for prime in primes:
    selected_primes.append(prime)
    n *= prime
    res = resilience(n)
    if res[2] < 15499/94744:
        print(res)
        break

# Now out problem becomes minimizing n
# To do that, we can try to remove the biggest prime from the list
# This will strongly reduce n and slightly reduce phi(n). If we fall below the desired ratio, we cann increase the exponent of the smallest prime
# To be precise, we have phi(n) = n * (1 - 1/factor1) * (1 - 1/factor2) * ... * (1 - 1/factorN) where factorN are the prime factors of n
# So we can redefine resilience as n * [product of (1 - 1/factorN)] / (n - 1)
# Lets assume for a moment our smallest prime factor is 2. If we remove the biggest prime factor, we can increase the exponent of 2 by 1
# So our new n will be n / biggest_prime * 2
# This leaves our resilience as n / biggest_prime * 2 * [product of (1 - 1/factorN)] / (n / biggest_prime * 2 - 1)
# At the same time, we know that the lower bound here is the resilience of leaving the biggest prime factor in the list and the exponents 1, so we only need
# to check with the biggest prime and can ignore the next biggest one
exponents = [1 for _ in selected_primes]
new_n = n

prime = selected_primes.pop()
print(f"Removing {prime}")
new_n //= prime
exponents[-1] += 1
res = resilience(new_n)
while res[2] > 15499/94744:
    exponents[0] += 1
    new_n *= selected_primes[0]
    res = resilience(new_n)
    print(f"New resilience for {new_n}: {res}")