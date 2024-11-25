from decimal import Decimal
# 15/21 * 14/20 = 1/2
# 85/120 * 84/119 = 1/2

# a/b * (a-1)/(b-1) = 1/2 =>
# (a * (a-1)) / (b * (b-1)) = 1/2 =>
# 2 * (a * (a-1)) = b * (b-1) =>
# 2 * a^2 - 2a = b^2 - b =>
# 2a^2 - 2a - b^2 + b = 0
# This equation can be solved using: 
# https://www.alpertron.com.ar/QUAD.HTM 
# TODO: Implement this at some point (see hermit normal form, smith normal form and diophantine equations)
# This gives the following equation:
# a_n+1 = 3a_n + 2b_n - 2
# b_n+1 = 4a_n + 3b_n - 3

# for a in range(1, 10000):
#     for b in range(1, 10000):
#         if 2*a**2 - 2*a == b**2 - b:
#             print(a, b)

# exit()

a, b = 15, 21

while b < 10**12:
    a, b = 3*a + 2*b - 2, 4*a + 3*b - 3

print(a, b)

# Answer: 756872327473