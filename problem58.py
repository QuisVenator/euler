import pyprimesieve as ps
from sortedcontainers import SortedList
import time

start = time.process_time()

primes = ps.primes(10**9)

# get ram usage
# gc.collect()
# process = psutil.Process(os.getpid())
# print(process.memory_info().rss/1024/1024)

primes = SortedList(primes)

# gc.collect()
# process = psutil.Process(os.getpid())
# print(process.memory_info().rss/1024/1024)

square_size = 1
total = 1
primes_count = 0

while True:
    square_size += 2
    total += 4
    down_right = square_size ** 2
    down_left = down_right - square_size + 1
    up_left = down_left - square_size + 1
    up_right = up_left - square_size + 1

    # down_right is always a square and thus not prime
    if down_left in primes:
        primes_count += 1
    if up_left in primes:
        primes_count += 1
    if up_right in primes:
        primes_count += 1
    
    # print(f"Square size: {square_size} - Primes count: {primes_count} - Total: {total} - Ratio: {primes_count / total}")
    if primes_count / total < 0.1:
        break

stop = time.process_time()
print(f"Time: {stop - start}")

print(square_size)
