from itertools import permutations

digits = [str(i) for i in range(10)]
pandigitals = permutations(digits)
pandigitals = [''.join(p) for p in pandigitals]

divisors = [None, 2, 3, 5, 7, 11, 13, 17]
cool_sum = 0
for pandigital in pandigitals:
    is_cool = True
    for j in range(1, 8):
        if int(pandigital[j:j+3]) % divisors[j] != 0:
            is_cool = False
            break
    if is_cool:
        cool_sum += int(pandigital)

print(cool_sum)