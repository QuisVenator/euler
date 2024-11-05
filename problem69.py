# We can calculate the totient like so:
# 1. Factorize the number
#
# Now, given these factors we can know the following for every factor:
#   1. The totient is at most n -1, as the factor is obviously not coprime with n
#   2. The totient is also at least n - n//factor, as all multiples of the factor are not coprime with n
#      2.1 We dont actually need to floor the division, seeing as we hava factor of n, n//factor will be an integer, so n - n/factor
#      2.2 We can simplify this to n * (1 - 1/factor)
#   3. Seeing that we can apply this for every factor, we note that for the second factor we can also substract n/factor2, but we need to add back the intersection of the factors
#      3.1 This leaves us with n * (1 - 1/factor1) - n/factor2 + n/(factor1 * factor2)  (again n/(factor1 * factor2) is an integer)
#      3.2 Simplifying we get n * (1 - 1/factor1) - n * (1/factor2 - 1/(factor1 * factor2))
#      3.3 Simplifying further we get n * (1 - 1/factor1 - 1/factor2 + 1/(factor1 * factor2)) or n * (1 - 1/factor1 + 1/(factor1 * factor2) - 1/factor2)
#      3.4 This might seem a familiar pattern, as we arrive at n * (1 - 1/factor1) * (1 - 1/factor2)
#   4. We can add like this all factors until we get the exact bond that phi(n) = n * (1 - 1/factor1) * (1 - 1/factor2) * ... * (1 - 1/factorN) where factorN are the prime factors of n


from common import phi

max_n_over_phi = 0
max_n = 0
for n in range(2, 1_000_001):
    n_over_phi = n / phi(n)
    if n_over_phi > max_n_over_phi:
        max_n_over_phi = n_over_phi
        max_n = n
    
    print(f"{n}", end='\r')
print()

print(max_n_over_phi)
print(max_n)
