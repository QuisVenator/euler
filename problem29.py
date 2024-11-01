distinct_power = set()

for a in range(2, 101):
    for b in range(2, 101):
        distinct_power.add(a ** b)

print(len(distinct_power))