import pyprimesieve

primes = pyprimesieve.primes(10**6)


square_primes = [x**2 for x in primes]
cube_primes = [x**3 for x in primes]
fourth_primes = [x**4 for x in primes]


numbers = set()
max_num = 50_000_000
for i, square in enumerate(square_primes):
    for j, cube in enumerate(cube_primes):
        if square + cube >= max_num:
            break
        
        for k, fourth in enumerate(fourth_primes):
            if square + cube + fourth < max_num:
                numbers.add(square + cube + fourth)
            else:
                break
            
    if i % 100 == 0:
        print(f"Progress: {i}, {i / len(square_primes) * 100:.2f}%", end="\r")

print()
print(len(numbers))

# Answer: 1097343
        