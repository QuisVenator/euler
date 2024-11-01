from itertools import permutations

# If they want us to do actual work for it they should have given us a number that is solved in a second the stupid way
def lexi_permu(n):
    return ''.join(list(permutations('0123456789'))[n-1])


print(lexi_permu(1_000_000))