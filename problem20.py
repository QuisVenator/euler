import math

fact = math.factorial(100)
fact_str = str(fact)
print(sum([int(digit) for digit in fact_str]))