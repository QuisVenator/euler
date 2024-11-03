import pyprimesieve as ps

primes = ps.primes(10**9)
primes_set = set(primes)

def check_both(a, b):
    return int(str(a) + str(b)) in primes_set and int(str(b) + str(a)) in primes_set

def create_permutations():
    index_million = 0
    while primes[index_million] < 10**4:
        index_million += 1
    for i1 in range(index_million):
        for i2 in range(i1+1, index_million):
            if not check_both(primes[i1], primes[i2]):
                continue
            for i3 in range(i2+1, index_million):
                if not check_both(primes[i1], primes[i3]) or not check_both(primes[i2], primes[i3]):
                    continue
                for i4 in range(i3+1, index_million):
                    if not check_both(primes[i1], primes[i4]) or not check_both(primes[i2], primes[i4]) or not check_both(primes[i3], primes[i4]):
                        continue
                    for i5 in range(i4+1, index_million):
                        if check_both(primes[i1], primes[i5]) and check_both(primes[i2], primes[i5]) and check_both(primes[i3], primes[i5]) and check_both(primes[i4], primes[i5]):
                            print(primes[i1], primes[i2], primes[i3], primes[i4], primes[i5])
                            print(sum([primes[i1], primes[i2], primes[i3], primes[i4], primes[i5]]))
                            return
        print(f"{i1 / index_million * 100:.2f}% Done")
                        


create_permutations()

