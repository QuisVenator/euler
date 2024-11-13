dp = {}

def fingerprint(n):
    return "".join(sorted(str(n)))

known_1 = [44,32,13,10,1]
known_89 = [85,89,145,42,20,4,16,37,58]

for i in known_1:
    dp[fingerprint(i)] = 1

for i in known_89:
    dp[fingerprint(i)] = 89

count = 0

for i in range(1, 10_000_000):
    n = fingerprint(i)
    chain = []
    while True:
        if n in dp:
            if dp[n] == 89:
                count += 1
            for x in chain:
                dp[x] = dp[n]
            break
        chain.append(n)
        n = sum([int(x) ** 2 for x in n])
        n = fingerprint(n)
    
    if i % 100_000 == 0:
        print(i, count)

    
print(count)