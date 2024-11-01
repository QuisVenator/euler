max = 0

for i in reversed(range(999)):
    for j in reversed(range(999)):
        candidate = i * j
        if candidate > max and str(candidate) == str(candidate)[::-1]:
            max = candidate

print(max)