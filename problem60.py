import pyprimesieve as ps
from threading import Thread, Event
import queue

primes = ps.primes(10**9)
primes_set = set(primes)

permutations = queue.Queue(maxsize=10)
solution_found = Event()

def check_permutation(permutation):
    for i in range(5):
        for j in range(i+1, 5):
            if not (int(str(permutation[i]) + str(permutation[j])) in primes_set and int(str(permutation[j]) + str(permutation[i])) in primes_set):
                return False
    return True
    

def check_primes():
    while not solution_found.is_set():
        try:
            permutation = permutations.get(timeout=1)
            if check_permutation(permutation):
                print(f"Solution: {permutation}, sum = {sum(permutation)}")
                solution_found.set()
        except queue.Empty:
            pass

def create_permutations():
    permutation_count = 0
    index_million = 0
    while primes[index_million] < 10**3:
        index_million += 1
    for i1 in range(index_million):
        for i2 in range(i1+1, index_million):
            for i3 in range(i2+1, index_million):
                for i4 in range(i3+1, index_million):
                    for i5 in range(i4+1, index_million):
                        # if solution_found.is_set():
                        #     break
                        # permutations.put([primes[i1], primes[i2], primes[i3], primes[i4], primes[i5]])
                        check_permutation([primes[i1], primes[i2], primes[i3], primes[i4], primes[i5]])
                        permutation_count += 1
                        if permutation_count % 1000 == 0:
                            print(f"{permutation_count} permutations created")
                            print(f"Progress: {i1 / index_million * 100:.2f}%")


# print(primes[-1])
# threads = [Thread(target=check_primes) for _ in range(12)]
# for t in threads:
#     t.start()

create_permutations()

# for t in threads:
#     t.join()

