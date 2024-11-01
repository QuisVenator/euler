index = 2

a = 1
b = 1
n = 10**999
while b < n:
    a, b = b, a + b
    index += 1

print(b)
print(len(str(b)))
print(index)