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
}


for k, v in known.items():
    k = "".join(sorted(k.replace("0", "1")))
    dp[k] = v +1

f = [0] * 10
for i in range(1, 10):
    f[i] = factorial(i)

sixty_long_count = 0
max_chain = 0
for i in reversed(range(1_000_000)):
    starts = "".join(sorted(str(i).replace("0", "1")))
    s = starts
    
    if starts in dp:
        if dp[starts] == 60:
            sixty_long_count += 1
        continue
    this_chain = 0

    prev = i
    while True:
        this_chain += 1
        next = 0
        for d in s:
            next += f[int(d)]
        s = "".join(sorted(str(next).replace("0", "1")))
        # print(next)
        if next == prev:
            break
        if s in dp:
            if  str(next) in known:
                this_chain -= 1
            this_chain += dp[s]
            # print("found", s, dp[s])
            break
        prev = next

    if this_chain == 60:
        sixty_long_count += 1
        # print(f"{i} is 60 long")
    if starts not in dp:
        dp[starts] = this_chain
    if dp[starts] > max_chain:
        # print(i)
        max_chain = dp[starts]

    # print(i, dp[starts])
    # print()
    # print()

print(sixty_long_count)
print(max_chain)
