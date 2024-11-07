from common import phi
import matplotlib.pyplot as plt
import pyprimesieve

# It seems that the resilience of d is always greatest, just before the next prime number.
# We can see this when we plot the data, but I have no formal proof for this.
# Set this value to True to see the trend (obviously, this slows the program down).:
plot_data = False
primes = pyprimesieve.primes(10**9)
print(f"Generated {len(primes)} primes.")

def resilience(d):
    return phi(d), d - 1, phi(d) / (d - 1)



if plot_data:
    d_data = []
    res_data = []
    for prime in primes[1:]:
        for x in [-1, 1]:
            d = prime + x
            res = resilience(d)
            d_data.append(d)
            res_data.append(res[2])
            if res[2] < 15499/94744:
                print(res)
                print(d)
                break
            d += 1
        if prime >= 30_000:
            break

    print(d)

    plt.plot(d_data, res_data)
    plt.show()

lowest_res = (0, 0, 1)
if not plot_data:
    for num, prime in enumerate(primes[1:]):
        for x in [-1, 1]:
            d = prime + x
            res = resilience(d)
            if res[2] < lowest_res[2]:
                lowest_res = res
            if res[2] < 15499/94744:
                print(res)
                print(d)
                exit()

        if num % 100 == 0:
            print(f"Checked {prime}, progress: {num / len(primes) * 100:.2f}%")
            print(lowest_res)
    

# Solution: 892_371_480