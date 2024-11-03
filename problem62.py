def fingerprint(n):
    fingerprint = ""
    for i in range(10):
        fingerprint += str(n.count(str(i))).zfill(3) + " "
    return fingerprint


permutation_count = {}

i = 1
while True:
    cube = i ** 3
    fp = fingerprint(str(cube))
    if fp in permutation_count:
        permutation_count[fp].append(cube)
    else:
        permutation_count[fp] = [cube]
    
    if len(permutation_count[fp]) == 5:
        print(permutation_count[fp])
        break
    i += 1