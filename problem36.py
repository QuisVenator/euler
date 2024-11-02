def is_palin(n):
    return str(n) == str(n)[::-1]

def is_palin_base2(n):
    return bin(n)[2:] == bin(n)[2:][::-1]


db_pali_sum = 0
for i in range(1, 1000000):
    if is_palin(i) and is_palin_base2(i):
        db_pali_sum += i

print(db_pali_sum)