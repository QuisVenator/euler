# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
#
# sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
# By expanding this for the first four iterations, we get:
#
# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
# The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
#
# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
#
import common as cm


# Generate the first 1000 expansions of sqrt(2)
def generate_expansion_rec_au(n):
    print(n)
    if n == 1:
        return "2"
    return f"2 + 1 / ({generate_expansion_rec(n - 1)})"

def generate_expansion_rec(n):
    return f"1 + 1 / ({generate_expansion_rec(n)})"

# Non recursive version
def generate_expansion(n):
    stack = []
    expression = "1 + 1 / ("
    stack.append(")")

    for i in range(n-1):
        expression += "2 + 1 / ("
        stack.append(")")
    
    expression += "2"
    expression += "".join(stack)
    return expression


count_more_digits = 0
for i in range(1, 1000):
    expr = generate_expansion(i)
    result = cm.evaluate_postfix(cm.tokens_to_fraction(cm.infix_to_postfix(expr)))
    if len(str(result.numerator)) > len(str(result.denominator)):
        count_more_digits += 1

    print(f"Progress: {i / 1000 * 100:.2f}%", end="\r")
print()

print(count_more_digits)
    