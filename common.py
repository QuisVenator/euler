import pyprimesieve


def proper_divisors(n) -> set:
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