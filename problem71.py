# Disregard, this was lucky but wrong

from dataclasses import dataclass
import pyprimesieve

# As this code shows, the number is always 10**n-numerator of right
# (uncomment to see example)
@dataclass
class fraction:
    numerator: int
    denominator: int
    fvalue: float

fractions = []
for i in range(1, 10):
    for j in range(1, i):
        if j % i == 0:
            continue
        fractions.append(fraction(j, i, j/i))

fractions.sort(key=lambda x: x.fvalue)

for i, f in enumerate(fractions):
    if f.numerator == 3 and f.denominator == 7:
        toprint = fractions[i-5:i+5]
        for f in toprint:
            print(f"{f.numerator}/{f.denominator}")
        break
    if f.numerator == 2 and f.denominator == 5:
        toprint = fractions[i-5:i+5]
        for f in toprint:
            print(f"{f.numerator}/{f.denominator}")
        print()

right_numerator = 3
right_denominator = 7

target_numerator = 1
target_denominator = 1_000_000 - right_numerator

for i in range(1, 1_000_000):
    if i / target_denominator > target_numerator / target_denominator and i / target_denominator < right_numerator / right_denominator:
        target_numerator = i

print(target_numerator)
print(target_denominator)

print(pyprimesieve.factorize(target_numerator))
print(pyprimesieve.factorize(target_denominator))


