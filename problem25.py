import time

start = time.process_time()
index = 2

a = 1
b = 1
n = 10**999
while b < n:
    a, b = b, a + b
    index += 1

stop = time.process_time()
print(f"Time: {stop - start}")
print(b)
print(len(str(b)))
print(index)