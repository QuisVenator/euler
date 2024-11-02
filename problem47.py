import pyprimesieve

consecutives = 0
start = None

n = 0
while True:
    n += 1
    factors = pyprimesieve.factorize(n)

    if len(factors) == 4:
        if start is None:
            start = n
            consecutives = 1
        else:
            consecutives += 1
            if consecutives == 4:
                print(f"Found: {start}")
                print(f"Factors {start}: {pyprimesieve.factorize(start)}")
                print(f"Factors {start + 1}: {pyprimesieve.factorize(start + 1)}")
                print(f"Factors {start + 2}: {pyprimesieve.factorize(start + 2)}")
                print(f"Factors {start + 3}: {pyprimesieve.factorize(start + 3)}")
                break
    else:
        start = None
        consecutives = 0
