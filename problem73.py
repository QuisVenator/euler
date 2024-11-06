import pyprimesieve
from itertools import combinations
# general idea:
# 1. get nearest fraction to both target fractions (above or below) with denominator d
# 2. get number of coprimes to d that are less than numerator of the obtained fractions
# 3. do this fast
# 4. save the difference and repeat for all d
# 4. profit

# floor symbol: ⌊ ⌋


# factors of 30: 2, 3, 5
# coprimes of 30 below 10: 1, 7
# 10 - ⌊10/2⌋ - ⌊10/3⌋ + ⌊10/6⌋ = 

# generalized formula: let a b c d be the factors
# n - ⌊n/a⌋ - ⌊n/b⌋ + ⌊n/lcm(a, b)⌋ - ⌊n/c⌋ + ⌊n/lcm(a, c)⌋ + ⌊n/lcm(b, c)⌋ - ⌊n/lcm(a, b, c)⌋ 
# + ⌊n/d⌋ - ⌊n/lcm(a, d)⌋ - ⌊n/lcm(b, d)⌋ - ⌊n/lcm(c, d)⌋ + ⌊n/lcm(a, b, d)⌋ + ⌊n/lcm(a, c, d)⌋ + ⌊n/lcm(b, c, d)⌋ - ⌊n/lcm(a, b, c, d)⌋
#
# because a, b, c and d are prime factors, the lcm is just the product of the factors
#
# if we reorder the terms, we get:
# n - ⌊n/a⌋ - ⌊n/b⌋ - ⌊n/c⌋ - ⌊n/d⌋ + ⌊n/lcm(a, b)⌋ + ⌊n/lcm(a, c)⌋ + ⌊n/lcm(a, d)⌋ + ⌊n/lcm(b, c)⌋ + ⌊n/lcm(b, d)⌋ + ⌊n/lcm(c, d)⌋ - ⌊n/lcm(a, b, c)⌋ - ⌊n/lcm(a, b, d)⌋ - ⌊n/lcm(a, c, d)⌋ - ⌊n/lcm(b, c, d)⌋ + ⌊n/lcm(a, b, c, d)⌋
#
# as a general algorithm we are left with:
# 1. get prime factors of d
# 2. get all combinations of the factors (call them factor_comb)
# 3. set result to n to start
# 4. subtract n // factor_comb[i] for every i where len(factor_comb[i]) is even
# 5. add n // factor_comb[i] for every i where len(factor_comb[i]) is odd








def coprimes_of_d_below_n(d, n):
    factors = pyprimesieve.factorize(d)
    factors = [x[0] for x in factors]

    result = n
    formula_string = f"{n}"
    for i in range(1, len(factors) + 1, 2):
        for comb in combinations(factors, i):
            # lcm of combination is multiplication of all factors
            lcm = 1
            # formula_string += f" - {n}//("
            for factor in comb:
                # formula_string += f"{factor} * "
                lcm *= factor
            # formula_string = formula_string[:-3] + ")"
            result -= n // lcm
    for i in range(2, len(factors) + 1, 2):
        for comb in combinations(factors, i):
            lcm = 1
            # formula_string += f" + {n}//("
            for factor in comb:
                # formula_string += f"{factor} * "
                lcm *= factor
            # formula_string = formula_string[:-3] + ")"
            result += n // lcm
    # print(formula_string)
    return result


# print(coprimes_of_d_below_n(15, 4))


def fractions_below(num_target, den_target, d):
    starting_num = num_target * d // den_target
    result = coprimes_of_d_below_n(d, starting_num)
    # print(f"{starting_num}/{d} is closest to {num_target}/{den_target} and has {result} coprimes below it")
    return result

lower_target_numerator = 1
lower_target_denominator = 3
upper_target_numerator = 1
upper_target_denominator = 2

total = 0
for d in range(2, 12_001):
    diff = fractions_below(upper_target_numerator, upper_target_denominator, d) - fractions_below(lower_target_numerator, lower_target_denominator, d)
    total += diff
    # print(f"Done with {d}, found {diff} between", end="\r\n")
# print()

# funnily enough, when the upper_target_denominator is in the range of d, the target upper fraction itself will also be counted, so to avoid this we need to subtract 1
print(total-1)

