import common

def is_perfect(n):
    return n == sum(common.proper_divisors(n))

def is_abundant(n):
    return n < sum(common.proper_divisors(n))

abundant_numbers = set()
for i in range(1, 28124):
    if is_abundant(i):
        abundant_numbers.add(i)

abundant_numbers_sorted = sorted(abundant_numbers)

not_writable_sum = 0
for i in range(1, 28124):
    can_be_written = False
    for j in abundant_numbers_sorted:
        if j > i:
            break
        if i - j in abundant_numbers:
            can_be_written = True
            break
    if not can_be_written:
        not_writable_sum += i

print(not_writable_sum)
