import math
from functools import cmp_to_key

def compare(base1, exp1, base2, exp2):
    if base1 == base2:
        if exp1 > exp2:
            return 1
        elif exp1 < exp2:
            return -1
        else:
            return 0
    
    if base1 >= base2 and exp1 >= exp2:
        return 1
    
    if base1 <= base2 and exp1 <= exp2:
        return -1
    
    return 1 if math.log2(base1) * exp1 >= math.log2(base2) * exp2 else -1

with open("inputs/0099_base_exp.txt") as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]
lines = [x.split(",") for x in lines]
lines = [[int(x[0]), int(x[1]), i+1] for i, x in enumerate(lines)]

lines.sort(key=cmp_to_key(lambda x, y: compare(x[0], x[1], y[0], y[1])))

print(lines[-1])

