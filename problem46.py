import pyprimesieve

primes = pyprimesieve.primes(10**5)
primes_set = set(primes)

squares = set()
squares.add(1)

max_square = 1

def get_next_square():
    global squares, max_square
    n = len(squares) + 1
    squares.add(n * n)
    max_square = n * n

def is_square(n):
    while n > max_square:
        get_next_square()
    return n in squares


n = 9
while True:
    n += 2
    if n in primes_set:
        continue

    is_goldbach = False
    for prime in primes:
        if prime > n:
            break
        if is_square((n - prime) // 2):
            is_goldbach = True
            break

    if not is_goldbach:
        print()
        print(f"Found: {n}")
        break
