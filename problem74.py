from math import factorial

dp = {}
known = {
    "169": 3,
    "363601": 3,
    "1454": 3,
    "871": 2,
    "45361": 2,
    "872": 2,
    "45362": 2,
    "1": 1,
}

for k, v in known.items():
    dp[int(k)] = v -1
    k = "".join(sorted(k.replace("0", "1")))
    dp[k] = v

f = [0] * 10
for i in range(1, 10):
    f[i] = factorial(i)

sixty_long_count = 0
max_chain = 0
for i in reversed(range(1_000_000)):
# for i in range(69,69+1):
    starts = "".join(sorted(str(i).replace("0", "1")))
    s = starts
    
    if starts in dp:
        if dp[starts] == 60:
            sixty_long_count += 1
        continue
    dp[starts] = 0

    prev = i
    while True:
        dp[starts] += 1
        next = 0
        for d in s:
            next += f[int(d)]
        s = "".join(sorted(str(next).replace("0", "1")))
        print(next)
        if next == prev:
            break
        if s in dp:
            dp[starts] += dp[s]
            print("found", s, dp[s])
            break
        prev = next

    if dp[starts] == 60:
        sixty_long_count += 1
        print(i, dp[starts])
    if dp[starts] > max_chain:
        print(i)
        max_chain = dp[starts]
    dp[i] = dp[starts] -1

    print(i, dp[starts])
    print()
    print()

print(sixty_long_count)
print(max_chain)
