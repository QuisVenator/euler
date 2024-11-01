import pyprimesieve

def get_divisor_count(n):
    factors = pyprimesieve.factorize(n)
    count = 1
    for fact in factors:
        count *= fact[1] + 1
    return count

triangle_num = 1
i = 2
while True:
    triangle_num += i
    i += 1
    c = get_divisor_count(triangle_num)
    print(triangle_num, c)
    if c > 500:
        break

print(triangle_num)