import math

i = 1
nine_fact = math.factorial(9)
while True:
    digit_fact = nine_fact * i
    max_num = 10 ** i - 1
    if digit_fact < max_num:
        break
    i += 1
    print(f"digits: {digit_fact} < num: {max_num}")

print(i) # We can only go up to 7 digits

sum_factorials = 0
for i in range(10, 10 ** i):
    if i == sum(math.factorial(int(c)) for c in str(i)):
        print(i)
        sum_factorials += i

print(sum_factorials)