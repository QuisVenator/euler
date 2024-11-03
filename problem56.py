max_digital_sum = 0

for a in range(1, 100):
    for b in range(1, 100):
        n = a ** b
        digital_sum = sum(int(d) for d in str(n))
        if digital_sum > max_digital_sum:
            max_digital_sum = digital_sum
    
    print(f"{a}% Done")

print(max_digital_sum)