from common import phi
import argparse

parser = argparse.ArgumentParser(description='Project Euler problem 72')
parser.add_argument('n', type=int, help='The upper bound for the denominator')

n = parser.parse_args().n
total = 0
for i in range(2, n+1):
    total += phi(i)

print(total)