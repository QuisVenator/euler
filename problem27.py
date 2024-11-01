import pyprimesieve

primes = pyprimesieve.primes(10000)
primes = set(primes)

max_n = 39
a = 0
b = 0
for i in range(-1001, 1001):
    for j in range(-1001, 1001):
        n = 40
        while n ** 2 + i * n + j in primes:
            n += 1
        n -= 1
        if n > max_n:
            # Verify it also works for lower n
            m = 0
            while m < 40 and m ** 2 + i * m + j in primes:
                m += 1
            if m == 40:
                max_n = n
                a = i
                b = j
                print(f"i: {i}, j: {j}, n: {n}, product: {i * j}")
    print(f"Tested n^2 + {i}n + j")

print(f"max_n: {max_n}")
print(f"a: {a}, b: {b}, product: {a * b}")