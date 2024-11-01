def reciprocal_len(n):
    remainders = {}
    remainder = 1
    while remainder not in remainders:
        remainders[remainder] = len(remainders)
        remainder = (remainder * 10) % n
    return len(remainders) - remainders[remainder]


max_reciprocal_len = 0
d = 0
for i in range(1, 1000):
    len_ = reciprocal_len(i)
    if len_ > max_reciprocal_len:
        max_reciprocal_len = len_
        d = i

print(f"d: {d}, len: {max_reciprocal_len}")