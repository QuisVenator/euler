from common import are_coprime
from itertools import count

def generate_pythagorean_triple_below(max_one_side):
    m = 1
    n = 1
    perimeters = 0

    while True:
        n = m + 1
        while True:
            if are_coprime(m, n):
                a = n**2 - m**2
                b = 2 * n * m
                c = n**2 + m**2
                a, b, c  = sorted([a, b, c])
                if c > max_one_side: # One side is 2*a and the other two sides that are equal are c
                    if n == m + 1:
                        return perimeters
                    break

                # We know that we can generate more triples by multiplying by a constant k, but
                # kc - 2ka = 1 => k * (c - 2a) = 1 => therefore k has to be one, so we are only interested in primitive triples
                if abs(c - 2 * a) == 1:
                    perimeters += 2 * (a + c)
                    print(perimeters)
                
                # for k in count(1):
                #     a = k * a
                #     b = k * b
                #     c = k * c
                #     p = 2 * (a + c)
                #     if p > max_perimeter:
                #         break

                #     if abs(c - 2 * a) == 1: 
                #         perimeters += p
            n += 2 # keeps n odd when m is even and vice versa
        m += 1


# print(area_is_int(333000000, 333000000, 333000001))
# print(area_is_int(5, 5, 6))

print(generate_pythagorean_triple_below(10**9//3))

# Answer: 518408346