import pyprimesieve

primes = pyprimesieve.primes(1000000)
primes_set = set(primes)

truncable_sum = 0
count = 0
for j, prime in enumerate(primes[4:]):
    truncable = True
    for i in range(1, len(str(prime))):
        if int(str(prime)[i:]) not in primes_set or int(str(prime)[:-i]) not in primes_set:
            truncable = False
            break
    
    print(f"Checking prime: {prime}, progress: {j}/{len(primes)} ({j/len(primes)*100}%)", end="\r")
    if truncable:
        truncable_sum += prime
        count += 1
        print()
        print(prime)
        if count == 11:
            break

print()
print(f"Sum of truncable primes: {truncable_sum}")