import math
pandigital = set()

def is_pandigital(n):
    digits = []
    while n > 0:
        digit = n % 10
        n //= 10

        if digit in digits or digit == 0:
            return False
        digits.append(digit)
    return True


max_multi = math.ceil(math.sqrt(987654322))
for i in range(1, max_multi):
    if is_pandigital(i):
        pandigital.add(i)

sorted_pandigital = sorted(pandigital)

super_pan = set()
for i, multiplicand in enumerate(sorted_pandigital):
    for multiplier in sorted_pandigital[i:]:
        product = multiplicand * multiplier
        if is_pandigital(product) and len(set(str(multiplicand) + str(multiplier) + str(product))) == len(str(multiplicand) + str(multiplier) + str(product)) == 9:
            print(f"{multiplicand} * {multiplier} = {product}")
            super_pan.add(product)


print(sum(super_pan))