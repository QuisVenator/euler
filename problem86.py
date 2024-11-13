squares = set([i**2 for i in range(1, 100_000)])

count = 0
for i in range(1, 20_000+1):
    i_squared = i**2
    for j in range(1, i+1):
        for k in range(1, j+1):
            l = i_squared + (j+k)**2
            if l in squares:
                count += 1
    
    if i % 10 == 0:
        print(f"Progress: {count}, {count / 1_000_000 * 100:.2f}%", end="\r")
    
    if count > 1_000_000:
        print()
        print(f"With M = {i}, the number of solutions exceeds 1,000,000 ({count})")
        break
