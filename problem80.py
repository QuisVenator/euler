from math import sqrt

def digits_of_sqrt(n,m):
    if sqrt(n).is_integer():
        return [0]

    n_str = str(n)
    p = 0
    digits = []


    remainder = 0
    c = 0
    p = 0

    while True:
        # Bring down leftmost digit pair
        if len(n_str) > 1:
            c = int(n_str[:2])
            n_str = n_str[2:]
        elif len(n_str) == 1:
            c = int(n_str[0])
            n_str = ""
        else:
            c = 0
        
        # Append c to remainder
        c = 100 * remainder + c

        # find greatest x such that x(20p + x) <= c
        x = c//(20*p) if p != 0 else 1
        while x * (20*p + x) < c:
            x += 1
        while x * (20*p + x) > c:
            x -= 1
        
        # append x to digits
        digits.append(x)

        # update remainder
        remainder = c - x * (20*p + x)

        # update p
        p = 10 * p + x

        if remainder == 0:
            return digits

        if len(digits) == m:
            return digits
        
        # print(f"p: {p}, c: {c}, x: {x}, remainder: {remainder}")
        
# print("".join([str(x) for x in digits_of_sqrt(2, 100)]))
# print(sum(digits_of_sqrt(2, 100)))
res  = 0
for i in range(1, 101):
    res += sum(digits_of_sqrt(i, 100))

print(res)