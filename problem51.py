import pyprimesieve

primes = pyprimesieve.primes(10**7)

families = {}

for num, prime in enumerate(primes):
    prime = str(prime)

    # or mask in range(1, 2**len(prime)):
    for mask in range(1, 2**len(prime)):
        mask = bin(mask)[2:].zfill(len(prime))

        family = ""
        repd = None
        for i in range(len(prime)):
            if mask[i] == "1":
                family += prime[i]
            else:
                if repd is None:
                    repd = prime[i]
                elif prime[i] != repd:
                    family = None
                    break
                family += "*"
        if family is None:
            continue
        if family not in families:
            families[family] = [prime, 1]
        else:
            families[family][1] += 1
            if families[family][1] == 8:
                print(f"Family: {family} - Prime: {families[family][0]}")
                exit()


    if num % 1000 == 0:
        print(f"{prime} - {num / len(primes) * 100:.2f}%")