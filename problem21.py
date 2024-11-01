import pyprimesieve

def proper_divisors(n):
    div = divisors(n)
    div.remove(n)
    return div

def divisors(n):
    factors = pyprimesieve.factorize(n)
    return proper_divisors_rec(factors, 0, 0, 1)

def proper_divisors_rec(factors, i, exponent, divisor):
    divisors = set()
    if i == len(factors):
        divisors.add(divisor)
        return divisors
    
    divisors.update(proper_divisors_rec(factors, i + 1, 0, divisor * factors[i][0] ** exponent))
    if exponent < factors[i][1]:
        divisors.update(proper_divisors_rec(factors, i, exponent + 1, divisor))

    return divisors


divisor_sums = {}
amicable_sum = 0
for i in range(1, 10_000):
    div_sum = sum(proper_divisors(i))
    if div_sum in divisor_sums and divisor_sums[div_sum] == i:
        amicable_sum += i + div_sum
    else:
        divisor_sums[i] = div_sum

# print()
# print(sorted(proper_divisors(220)))
# print(sorted(proper_divisors(284)))
# print(sum(proper_divisors(220)))
# print(sum(proper_divisors(284)))

print(amicable_sum)