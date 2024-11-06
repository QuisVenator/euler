from common import gcd, closest_fraction_to_with_max_d
import time

start = time.process_time()

def reduce_fraction(numerator, denominator):
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor

right_numerator = 3
right_denominator = 7

stop = time.process_time()

print(stop - start)

result_numerator, result_denominator = closest_fraction_to_with_max_d(right_numerator, right_denominator, 1000000)
print(result_numerator, result_denominator)
print(reduce_fraction(result_numerator, result_denominator))

