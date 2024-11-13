# from common import divisors
import sys
sys.setrecursionlimit(10**6)

def divisors(n):
    divs = []
    for i in range(2, n//2 + 1):

        if n % i == 0:
            divs.append(i)
    
    divs.append(n)
    return divs
            

# We can know that the max N for any k is 2k, as when N = 2k we can  make  1 * ... * 1 * 2 * k = 1 + ... + 1 + 2 + k
# and if we have k terms, than k-2 of them must be 1, so we have k-2 + 2 + k = 2k = N
div_k = [divisors(i) for i in range(24001)]

print("Divisors calculated")
print(div_k[:10])

min_k = [0 for i in range(12001)]
k_not_found = 12000 - 1

lowest_unfound_k = 2

def integer_partition(n, remaining_prod, remaining_sum, k, last_divisor=float("inf")): 
    global k_not_found, min_k, lowest_unfound_k

    if k > 12000:
        return
    
    if k + remaining_sum < lowest_unfound_k:
        return

    if remaining_prod == 1:
        true_k = k + remaining_sum
        if true_k < 12001 and min_k[true_k] == 0:
            min_k[true_k] = n
            k_not_found -= 1
            for i in range(lowest_unfound_k, 12001):
                if min_k[i] == 0:
                    lowest_unfound_k = i
                    break

            if k_not_found == 0:
                return
    
    if remaining_sum < remaining_prod:
        return
    
    for i in div_k[remaining_prod]:
        if i > last_divisor:
            break
        # print(f"n: {n}, remaining_prod: {remaining_prod}, remaining_sum: {remaining_sum}, k: {k}, i: {i}")
        integer_partition(n, remaining_prod // i, remaining_sum-i, k+1, i)
        
        if k_not_found == 0:
            return

test_num = 4
while k_not_found > 0:
    integer_partition(test_num, test_num, test_num, 0)
    test_num += 1

    if test_num % 100 == 0:
        print(f"Progress: {k_not_found}")
        print(test_num)

print(sum(set(min_k)))
print(min_k)
