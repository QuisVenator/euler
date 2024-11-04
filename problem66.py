from decimal import Decimal
import math
import time

start = time.process_time()

multipliers = []
for i in range(2, 1001):
    if (i ** 0.5) % 1 == 0:
        continue
    multipliers.append(i)
# multipliers = [13]


max_y = 0
max_d = 0
x = 1
while True:
    square = x ** 2
    to_remove = []
    for m in multipliers:
        future = square * m + 1
        future_sqr = Decimal(future).sqrt()
        if future_sqr % 1 == 0:
            to_remove.append(m)
            if future_sqr > max_y:
                max_y = future_sqr
                max_d = m
                print(f"Found {max_y}^2 - {max_d} * {x}^2 = 1")
                print(f"Found solution for {m} with x = {x}")
                print(f"Remaining multipliers: {len(multipliers) - len(to_remove)}")
    for m in to_remove:
        multipliers.remove(m)
    if len(multipliers) == 0:
        break
    x += 1

stop = time.process_time()

print(max_y)
print(max_d)

print(f"Time: {stop - start}")