from common import gcd
import time
import cProfile

start = time.process_time()

def reduce_fraction(numerator, denominator):
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor

right_numerator = 3
right_denominator = 7
smallest_diff = 1
result_numerator = 0
result_denominator = 0
# We obviously need to check only one option for each denominator, this being the one that brings it closest to 3/7
# We have 3/7 > x/i
# We change this to 3i/7 > x, so the obvious candidate is to check the floor of 3i/7
# So if i is a multiple of 7, we get an integer and therefore the floor is equal not greater (thats why we skip multiples of 7)
# It could still be, that floor(3i/7)/i is not a proper fraction, but for that we just reduce the fraction

def resolve():
    global smallest_diff, result_numerator, result_denominator
    for i in reversed(range(1, 1000000)):
        if i % 7 == 0 or (3 * i) % 7 == 0:
            continue
        numerator = (3 * i) // 7

        diff = 3 / 7 - numerator / i
        if diff < smallest_diff:
            smallest_diff = diff
            result_numerator = numerator
            result_denominator = i

cProfile.run('resolve()')

stop = time.process_time()

print(stop - start)

print(result_numerator, result_denominator)
print(reduce_fraction(result_numerator, result_denominator))

