fractions = []

for i in range(10,100):
    for j in range(i,100):
        if i != j and i % 10 != 0 and j % 10 != 0:
            a = str(i)
            b = str(j)
            if a[0] == b[0] and int(a[1]) / int(b[1]) == i / j:
                print(f"{i}/{j} = {a[1]}/{b[1]}")
                fractions.append((i, j))
            if a[0] == b[1] and int(a[1]) / int(b[0]) == i / j:
                print(f"{i}/{j} = {a[1]}/{b[0]}")
                fractions.append((i, j))
            if a[1] == b[0] and int(a[0]) / int(b[1]) == i / j:
                print(f"{i}/{j} = {a[0]}/{b[1]}")
                fractions.append((i, j))
            if a[1] == b[1] and int(a[0]) / int(b[0]) == i / j:
                print(f"{i}/{j} = {a[0]}/{b[0]}")
                fractions.append((i, j))

print(fractions)

# get product of fractions, then get lowest common denominator
numerator = 1
denominator = 1
for fraction in fractions:
    numerator *= fraction[0]
    denominator *= fraction[1]
print(numerator, denominator)

# simplify fraction
for i in range(2, numerator + 1):
    while numerator % i == 0 and denominator % i == 0:
        numerator //= i
        denominator //= i

print(numerator, denominator)