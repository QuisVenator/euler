from dataclasses import dataclass

@dataclass
class irrational_square_root:
    whole_part: int
    repeating_part: list

def get_irrational_square_root(n: int) -> irrational_square_root:
    whole_part = int(n ** 0.5)
    repeating_part = []
    

    known = set()
    subtrahend = whole_part
    numerator = 1
    while True:
        known.add((subtrahend, numerator))
        denominator = n - subtrahend ** 2

        denominator = denominator // numerator
        numerator = 1

        a = int((numerator * (whole_part + subtrahend)) / denominator)
        repeating_part.append(a)
        subtrahend = (numerator * (whole_part + subtrahend)) - (a * denominator) - whole_part
        subtrahend = -subtrahend

        numerator = denominator
        if (subtrahend, numerator) in known:
            break

    return irrational_square_root(whole_part, repeating_part)

# print(get_irrational_square_root(7))

odd_period = 0
for i in range(1, 10_001):
    if (i ** 0.5) % 1 == 0:
        continue
    irsq = get_irrational_square_root(i)
    if len(irsq.repeating_part) % 2 == 1:
        odd_period += 1
    
    print(i, end='\r')
print()

print(odd_period)



    