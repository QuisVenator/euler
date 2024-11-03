from itertools import permutations

triangles = []
squares = []
pentagonals = []
hexagonals = []
heptagonals = []
octagonals = []


# Generate triangle numbers with 4 digits
n = 0
while True:
    n += 1
    t = n * (n + 1) // 2
    if t >= 1000 and t < 10000:
        triangles.append(t)
    if t >= 10000:
        break

# Generate square numbers with 4 digits
n = 0
while True:
    n += 1
    s = n ** 2
    if s >= 1000 and s < 10000:
        squares.append(s)
    if s >= 10000:
        break

# Generate pentagonal numbers with 4 digits
n = 0
while True:
    n += 1
    p = n * (3 * n - 1) // 2
    if p >= 1000 and p < 10000:
        pentagonals.append(p)
    if p >= 10000:
        break

# Generate hexagonal numbers with 4 digits
n = 0
while True:
    n += 1
    h = n * (2 * n - 1)
    if h >= 1000 and h < 10000:
        hexagonals.append(h)
    if h >= 10000:
        break

# Generate heptagonal numbers with 4 digits
n = 0
while True:
    n += 1
    he = n * (5 * n - 3) // 2
    if he >= 1000 and he < 10000:
        heptagonals.append(he)
    if he >= 10000:
        break
    
# Generate octagonal numbers with 4 digits
n = 0
while True:
    n += 1
    o = n * (3 * n - 2)
    if o >= 1000 and o < 10000:
        octagonals.append(o)
    if o >= 10000:
        break
    
print("Done generating numbers")
num_sets = [squares, pentagonals, hexagonals, heptagonals, octagonals]
used = [False] * 5

def find_cycle(num_sets, used, cycle):
    if all(used):
        if str(cycle[-1])[2:] == str(cycle[0])[:2]:
            print(cycle)
            print(sum(cycle))
            exit()
    
    for i in range(5):
        if not used[i]:
            for num in num_sets[i]:
                if str(cycle[-1])[2:] == str(num)[:2]:
                    used[i] = True
                    cycle.append(num)
                    find_cycle(num_sets, used, cycle)
                    cycle.pop()
                    used[i] = False

for num in triangles:
    find_cycle(num_sets, used, [num])