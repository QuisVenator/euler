
pentagonals = []
pentagonals_set = set()

def get_next_pentagonal():
    n = len(pentagonals) + 1
    pentagonals.append(n * (3 * n - 1) // 2)
    pentagonals_set.add(pentagonals[-1])

get_next_pentagonal()
get_next_pentagonal()

d = float('inf')
i = 0
while pentagonals[-1] - pentagonals[-2] < d:
    for subst in pentagonals[:-1]:
        difference = pentagonals[-1] - subst
        if subst > difference:
            break
        if difference in pentagonals_set and difference-subst in pentagonals_set:
            print(f"Found: {difference} - {subst} with difference {difference - subst}")
            d = min(d, difference - subst)
    i += 1
    if i % 10000 == 0:
        print(f"{pentagonals[-1] - pentagonals[-2]} < {d}")
    get_next_pentagonal()
    
print(d)