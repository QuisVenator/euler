fifth_powers = {}

for i in range(10):
    fifth_powers[i] = i ** 5

max_sum = 5 * fifth_powers[9]

sum_posibilities = 0
for i in range(2, max_sum):
    if i == sum(fifth_powers[int(c)] for c in str(i)):
        sumstring = " + ".join(f"{c}^5" for c in str(i))
        print(f"{i}= {sum(fifth_powers[int(c)] for c in str(i))} = {sumstring}")
        sum_posibilities += i

print(sum_posibilities)