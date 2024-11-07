
with open('inputs/0079_keylog.txt') as f:
    keylog = f.readlines()

keylog = [x.strip() for x in keylog]
for i in range(len(keylog)):
    key = []
    for j in range(len(keylog[i])):
        key.append(int(keylog[i][j]))
    keylog[i] = key
        

used = [0 for _ in keylog]
used_count = 0

passcode = [-1] * len(keylog) * 3

def solve(current_best=8, depth=0):
    global passcode, used, keylog, used_count
    if used_count == len(keylog)*3:
        return 0
    
    if depth >= current_best:
        return 450

    remaining = current_best - depth + 1
    for i in range(10):
        changed = []
        for j in range(len(keylog)):
            if used[j] == 3:
                continue
            if i == keylog[j][used[j]]:
                used[j] += 1
                changed.append(j)
                used_count += 1
            
        if len(changed) > 0:
            candidate = solve(current_best, depth + 1) + 1
            if candidate < remaining:
                remaining = candidate
                current_best = remaining + depth
                passcode[depth] = i
        
        for j in changed:
            used[j] -= 1
            used_count -= 1
    
    return remaining

# We bruteforce from shortest passcode, this means some duplicate calculations, but is still faster than starting at max length
max_len = 1
length = solve(max_len)
while length > max_len:
    max_len += 1
    length = solve(max_len)

print(length)
print("".join([str(x) for x in passcode[:length]]))

