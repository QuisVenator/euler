peri_solutions_dict = {}

for a in range(1, 1001):
    for b in range(a, 1001):
        if a + b >= 1000:
            break
        for c in range(b, 1001):
            perimeter = a + b + c
            if perimeter > 1000:
                break
            if a**2 + b**2 == c**2:
                if perimeter in peri_solutions_dict:
                    peri_solutions_dict[perimeter].append((a, b, c))
                else:
                    peri_solutions_dict[perimeter] = [(a, b, c)]

max_solutions = 0
max_perimeter = None
for key in peri_solutions_dict:
    if len(peri_solutions_dict[key]) > max_solutions:
        max_solutions = len(peri_solutions_dict[key])
        max_perimeter = key

print(f"Perimeter with most solutions: {max_perimeter}")
print(f"Number of solutions: {max_solutions}")
print(f"Solutions: {peri_solutions_dict[max_perimeter]}")