from math import factorial as fact

def combi(n, r):
    return fact(n) / (fact(r) * fact(n - r))

count = 0
for n in range(1, 101):
    for r in range(1, n):
        if combi(n, r) > 1000000:
            count += 1

print(count)
        