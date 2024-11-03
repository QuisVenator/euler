# I guess we have to fucking assume that nth power means a SINGLE DIGIT number to n?? Why?! who the fuck knows
# With that assumption the numbers or the exponent escape at some point (I am certain there is nice mathematical proof, but I say the escape if for 100 iterations the number had more digits than the exponent)

powerfull_digit_counts = 1
for base in range(2, 10):
    power = 1
    bs_assumption1 = 0
    bs_assumption2 = 0
    while True:
        n = base ** power
        if len(str(n)) == power:
            powerfull_digit_counts += 1
        elif len(str(n)) > power:
            bs_assumption1 += 1
            if bs_assumption1 > 100:
                break
        else:
            bs_assumption2 += 1
            if bs_assumption2 > 100:
                break
        power += 1
    
print(powerfull_digit_counts)
