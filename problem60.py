import pyprimesieve as ps
from itertools import permutations
from threading import Thread, Lock

primes = ps.primes(10**9)

prime_set = set(primes)

i = 0
index_lock = Lock()

def check_prime(prime):
    prime = str(prime)

    for s1 in range(1, len(prime)):
        for s2 in range(s1+1, len(prime)):
            for s3 in range(s2+1, len(prime)):
                for s4 in range(s3+1, len(prime)):
                    p1 = int(prime[:s1])
                    p2 = int(prime[s1:s2])
                    p3 = int(prime[s2:s3])
                    p4 = int(prime[s3:s4])
                    p5 = int(prime[s4:])
                    if len(set([p1, p2, p3, p4, p5])) != 5:
                        continue
                    if all([p1 in prime_set, p2 in prime_set, p3 in prime_set, p4 in prime_set, p5 in prime_set]):
                        # try all permutations
                        for perm in permutations([p1, p2, p3, p4, p5]):
                            if all([int("".join(map(str, perm))) in prime_set for perm in permutations([p1, p2, p3, p4, p5])]):
                                print(sum(perm))
                                exit()
    

def check_primes():
    global i
    while True:
        with index_lock:
            if i >= len(primes):
                return
            prime = primes[i]
            i += 1
        if i % 1000 == 0:
            print(f"{prime} - {i / len(primes) * 100:.2f}%")
        check_prime(prime)


threads = [Thread(target=check_primes) for _ in range(12)]
for t in threads:
    t.start()

for t in threads:
    t.join()
    
