import pyprimesieve

factors = []
for i in range(2, 21):
    factors.append(pyprimesieve.factorize(i))

print(factors)

mcm_factors = {}
for fact_l in factors:
    for fact in fact_l:
        if fact[0] not in mcm_factors:
            mcm_factors[fact[0]] = fact[1]
        else:
            mcm_factors[fact[0]] = max(mcm_factors[fact[0]], fact[1])

res = 1
for fact, exp in mcm_factors.items():
    res *= fact ** exp

print(res)