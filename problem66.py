import math

multipliers = []
for i in range(2, 1001):
    if (i ** 0.5) % 1 == 0:
        continue
    multipliers.append(i)


max_x = 0
x = 1
while True:
    square = x ** 2
    to_remove = []
    for m in multipliers:
        future = square * m + 1
        if math.sqrt(future) % 1 == 0:
            to_remove.append(m)
            max_x = x
            print(f"Found solution for {m} with x = {x}")
            print(f"Remaining multipliers: {len(multipliers) - len(to_remove)}")
    for m in to_remove:
        multipliers.remove(m)
    if len(multipliers) == 0:
        break
    x += 1

print(max_x)
