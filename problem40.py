# Once again, there is probably a nice solution to this problem
# But I have a computer created after 1980, so I don't care
digits = ""
i = 0
while len(digits) < 1000000:
    i += 1
    digits += str(i)

product = 1
for i in range(7):
    product *= int(digits[10**i - 1])

print(product)