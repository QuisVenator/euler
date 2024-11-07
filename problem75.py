from math import sqrt
from common import are_coprime

# euclids formula for generating pythagorean triples:
# a = m^2 - n^2 ; b = 2mn ; c = m^2 + n^2
# for some m > n > 0
# Proof:
# a^2 = m^4 - 2m^2n^2 + n^4
# b^2 = 4m^2n^2
# c^2 = m^4 + 2m^2n^2 + n^4
# a^2 + b^2 = m^4 - 2m^2n^2 + n^4 + 4m^2n^2 = m^4 + 2m^2n^2 + n^4 = c^2
# m^4 - 2m^2n^2 + n^4 + 4m^2n^2 = m^4 + 2m^2n^2 + n^4
# m^4 + n^4 = m^4 + n^4

# we can generate all primitive triples by setting m and n to be coprime
# and one of them to be even, the other odd


#n^2: 1 4 9 16 25 36 49 64 81 100
#m^2: 1 4 9 16 25 36 49 64 81 100

# 5 = n^2 - m^2
# 12 = 2nm
# 13 = n^2 + m^2

def solve(max_l):
    m = 1
    n = 1
    triples = {}

    while True:
        n = m + 1
        while True:
            if are_coprime(m, n):
                a = n**2 - m**2
                b = 2 * n * m
                c = n**2 + m**2
                p = a + b + c
                if p > max_l:
                    if n == m + 1:
                        return triples
                    break
                
                while p <= max_l:
                    if p in triples:
                        triples[p] += 1
                    else:
                        triples[p] = 1
                    # Equivalent to multiplying by 1 more
                    p += a + b + c
            n += 2 # keeps n odd when m is even and vice versa

        m += 1

triples = solve(1_500_000)
count = 0
for k, v in triples.items():
    # print(k, v)
    if v == 1:
        count += 1

print(count)

