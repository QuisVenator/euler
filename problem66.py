from common import get_irrational_square_root, evaluate_postfix, tokens_to_fraction, infix_to_postfix
import time

start = time.process_time()

multipliers = []
for i in range(2, 1001):
    if (i ** 0.5) % 1 == 0:
        continue
    multipliers.append(i)
# multipliers = [2,7,13,23]

max_x = 0
d_for_max_x = 0
for m in multipliers:
    sqr = get_irrational_square_root(m)
    expr = ""
    if len(sqr.repeating_part) % 2 == 1:
        expr = sqr.generate_expansion(len(sqr.repeating_part) * 2)
    else:
        expr = sqr.generate_expansion(len(sqr.repeating_part))
    
    # print(expr)

    fraction = evaluate_postfix(tokens_to_fraction(infix_to_postfix(expr)))
    # print(m, fraction)
    if fraction.numerator > max_x:
        max_x = fraction.numerator
        d_for_max_x = m
        

stop = time.process_time()

print(f"Result: {d_for_max_x} ({max_x})")

print(f"Time: {stop - start}")