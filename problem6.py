sum = 0
for i in range(1, 101):
    sum += i

sum_squared = sum ** 2

squared_sum = 0
for i in range(1, 101):
    squared_sum += i ** 2

print(sum_squared - squared_sum)