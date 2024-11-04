from common import get_irrational_square_root


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



    