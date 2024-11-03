

def is_lyrchel_below_50(n):
    for i in range(50):
        n += int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return False
    return True

count = 0
for i in range(10**4):
    if is_lyrchel_below_50(i):
        count += 1

print(count)