from itertools import permutations
import common

digits = "123456789"
pandigital = set()

for perm in permutations(digits):
    perm = "".join(perm)
    pandigital.add(int(perm))

sorted_pandigital = sorted(pandigital, reverse=True)

largest_possible = None
for i, candidate in enumerate(sorted_pandigital):
    divisors = common.proper_divisors(candidate)

    for divisor in divisors:
        concat = ""
        for j in range(1, 10):
            if divisor * j > candidate:
                break
            concat += str(divisor * j)
            if int(concat) == candidate:
                largest_possible = candidate
                print()
                print(f"Found pandigital number: {candidate}")
                exit()

    # print progress (round to 2 decimal places)
    print(f"Progress: {i}/{len(sorted_pandigital)} ({round(i/len(sorted_pandigital)*100, 2)}%)", end="\r")